import math
import numpy as np


def ibvs(target, image_width, image_height, cfg=None):

    cfg = cfg or {}

    fov = cfg.get("fov", 60)
    desired_area = cfg.get("area", 0.02)
    distance = cfg.get("z", 25)
    gain = cfg.get("lam", 0.8)
    theta = cfg.get("theta", 55)

    box = target["box"] if isinstance(target, dict) else target
    x1, y1, x2, y2 = map(float, box)

    # Camera focal length
    focal = (image_height / 2) / math.tan(
        math.radians(fov / 2)
    )

    # Target position in the image
    x = ((x1 + x2) / 2 - image_width / 2) / focal
    y = ((y1 + y2) / 2 - image_height / 2) / focal

    # Target apparent size
    area = (x2 - x1) * (y2 - y1)

    rho = math.log(math.sqrt(
        area / (image_width * image_height)
    ))

    rho_desired = math.log(math.sqrt(desired_area))

    # Image error
    error = np.array([
        x,
        y,
        rho - rho_desired
    ])

    # Estimate target distance
    Z = distance * math.exp(rho_desired - rho)

    # Simplified interaction matrix
    L = np.array([
        [-1, 0, x],
        [0, -1, y],
        [0, 0, 1]
    ])

    # Calculate movement
    vx, vy, vz = -gain * Z * (L @ error)

    angle = math.radians(theta)

    commands = {
        "r": float(vx),
        "f": float(-vy * math.sin(angle) + vz * math.cos(angle)),
        "u": float(-vy * math.cos(angle) - vz * math.sin(angle))
    }

    return commands, error.tolist()
