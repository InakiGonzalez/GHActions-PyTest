def calcular_area(b, h):
    if b < 0 or h < 0:
        raise ValueError("Base and height must be non-negative")
    if b == 0 or h == 0:
        raise ValueError("Base and height must be non-zero")
    return (b * h) / 2
