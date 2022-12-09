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
        length = float(length)
    except ValueError:
        length = 'ValErr_l'
    
    try:
        width = float(width)
    except ValueError:
        width = 'ValErr_w'
    
    if length == 'ValErr_l' and width == 'ValErr_w':
        return 'ValErr', length, width
    elif length == 'ValErr_l' or width == 'ValErr_w':
        return None, length, width
    else:
        area = f'{length * width:.2f}'
        return area, length, width

def square_area(side):
    try:
        area = f'{float(side) ** 2:.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return area

def tri_area(base, height):
    try:
        base = float(base)
    except ValueError:
        base = 'ValErr_b'
    
    try:
        height = float(height)
    except ValueError:
        height = 'ValErr_h'
    
    if base == 'ValErr_b' and height == 'ValErr_h':
        return 'ValErr', base, height
    elif base == 'ValErr_b' or height == 'ValErr_h':
        return None, base, height
    else:
        area = f'{0.5 * base * height:.2f}'
        return area, base, height

rect_area(1, 'c')
