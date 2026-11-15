import math
import numpy as np


def ibvs(target, image_width, image_height, cfg):

    x1, y1, x2, y2 = target["box"]

    fy = (image_height / 2) / math.tan(
        math.radians(cfg["fov"] / 2)
    )

    x = ((x1 + x2) / 2 - image_width / 2) / fy
    y = ((y1 + y2) / 2 - image_height / 2) / fy

    area = (x2 - x1) * (y2 - y1)

    rho = math.log(
        math.sqrt(area / (image_width * image_height))
    )

    rho_desired = math.log(math.sqrt(cfg["area"]))

    error = np.array([
        x,
        y,
        rho - rho_desired
    ])

    Z = cfg["z"] * math.exp(rho_desired - rho)

    L = np.array([
        [-1, 0, x],
        [0, -1, y],
        [0, 0, 1]
    ])

    vx, vy, vz = -cfg["lam"] * Z * (L @ error)

    angle = math.radians(cfg["theta"])

    commands = {
        "r": float(vx),
        "f": float(-vy * math.sin(angle) + vz * math.cos(angle)),
        "u": float(-vy * math.cos(angle) - vz * math.sin(angle))
    }

    return commands, error.tolist()
