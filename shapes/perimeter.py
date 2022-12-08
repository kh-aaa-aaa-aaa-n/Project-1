from math import pi

def circ_circumference(radius):
    try:
        circumference = f'{2 * pi * float(radius):.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return circumference

def rect_perimeter(length, width):
    try:
        perimeter = f'{float(length) * 2 + float(width) * 2:.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return perimeter

def square_perimeter(side):
    try:
        perimeter = f'{float(side) * 4:.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return perimeter

def tri_perimeter(side1, side2, side3):
    try:
        perimeter = f'{float(side1) + float(side2) + float(side3):.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return perimeter