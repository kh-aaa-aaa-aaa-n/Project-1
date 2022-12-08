from math import pi

def circ_area(radius):
    try:
        area = f'{pi * float(radius) ** 2:.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return area

def rect_area(length, width):
    try:
        area = f'{float(length) * float(width):.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return area

def square_area(side):
    try:
        area = f'{float(side) ** 2:.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return area

def tri_area(base, height):
    try:
        area = f'{0.5 * float(base) * float(height):.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return area