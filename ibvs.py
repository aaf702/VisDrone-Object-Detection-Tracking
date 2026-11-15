
"""
Image-Based Visual Servoing (IBVS)

Calculates drone motion commands from the target position and
apparent size in the camera image.
"""

import math
import numpy as np


def ibvs(target, image_width, image_height, cfg=None):
    """
    Args:
        target:
            ByteTrack result dictionary containing "box",
            or a bounding box [x1, y1, x2, y2].

        image_width: Image width in pixels.
        image_height: Image height in pixels.

        cfg: Optional IBVS configuration:
            fov   = vertical camera field of view in degrees
            area  = desired target area as a fraction of image area
            z     = reference distance
            lam   = control gain
            theta = camera/drone frame rotation in degrees

    Returns:
        commands: Dictionary containing r, f, u.
        error: Image feature error.
    """

    # Default configuration
    cfg = cfg or {}

    fov = cfg.get("fov", 60.0)
    desired_area = cfg.get("area", 0.02)
    distance = cfg.get("z", 25.0)
    gain = cfg.get("lam", 0.8)
    theta = cfg.get("theta", 55.0)

    # Validate image dimensions
    if image_width <= 0 or image_height <= 0:
        raise ValueError("Image dimensions must be positive.")

    # Validate camera and control parameters
    if not 0 < fov < 180:
        raise ValueError("FOV must be between 0 and 180 degrees.")

    if not 0 < desired_area < 1:
        raise ValueError("Desired area must be between 0 and 1.")

    if distance <= 0 or gain < 0:
        raise ValueError("Distance must be positive and gain non-negative.")

    # Get target bounding box
    if isinstance(target, dict):
        box = target["box"]
    else:
        box = target

    if len(box) != 4:
        raise ValueError("Bounding box must contain [x1, y1, x2, y2].")

    x1, y1, x2, y2 = map(float, box)

    box_width = x2 - x1
    box_height = y2 - y1

    if box_width <= 0 or box_height <= 0:
        raise ValueError("Invalid target bounding box.")

    # Calculate camera focal length from vertical FOV
    focal_length = (image_height / 2) / math.tan(
        math.radians(fov / 2)
    )

    # Normalize target center relative to image center
    x = ((x1 + x2) / 2 - image_width / 2) / focal_length
    y = ((y1 + y2) / 2 - image_height / 2) / focal_length

    # Calculate logarithmic target scale
    target_area = box_width * box_height

    rho = math.log(
        math.sqrt(
            max(target_area, 1.0) /
            (image_width * image_height)
        )
    )

    # Desired target scale
    rho_desired = math.log(math.sqrt(desired_area))

    # Image feature error
    error = np.array([
        x,
        y,
        rho - rho_desired
    ])

    # Estimate target depth
    Z = distance * math.exp(rho_desired - rho)

    # Simplified interaction matrix used by this project
    interaction_matrix = np.array([
        [-1,  0,  x],
        [ 0, -1,  y],
        [ 0,  0,  1.0]
    ])

    # Calculate camera-relative velocity components
    vx, vy, vz = -gain * Z * (interaction_matrix @ error)

    # Transform commands using the configured angle
    angle = math.radians(theta)

    commands = {
        "r": float(vx),
        "f": float(-vy * math.sin(angle) + vz * math.cos(angle)),
        "u": float(-vy * math.cos(angle) - vz * math.sin(angle))
    }

    return commands, error.tolist()


# Example test
if __name__ == "__main__":

    target = {
        "box": [400, 200, 560, 360]
    }

    config = {
        "fov": 60.0,
        "area": 0.02,
        "z": 25.0,
        "lam": 0.8,
        "theta": 55.0
    }

    commands, error = ibvs(
        target,
        image_width=960,
        image_height=540,
        cfg=config
    )

    print("Motion commands:", commands)
    print("Image error:", error)
