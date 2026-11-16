def ibvs(box, image_width, image_height):

    if box is None:
        return {"r": 0, "u": 0, "f": 0}

    x1, y1, x2, y2 = box

    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    error_x = (cx - image_width / 2) / (image_width / 2)
    error_y = (cy - image_height / 2) / (image_height / 2)

    width_ratio = (x2 - x1) / image_width

    desired_width = 0.20

    r = -0.5 * error_x
    u = -0.5 * error_y
    f = 0.5 * (desired_width - width_ratio)

    r = max(-1, min(1, r))
    u = max(-1, min(1, u))
    f = max(-1, min(1, f))

    return {
        "r": r,
        "u": u,
        "f": f
    }
