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
        perimeter = f'{length * 2 + width * 2:.2f}'
        return perimeter, length, width

def square_perimeter(side):
    try:
        perimeter = f'{float(side) * 4:.2f}'
    except ValueError:
        return 'ValErr'
    else:
        return perimeter

def tri_perimeter(side1, side2, side3):
    try:
        side1 = float(side1)
    except ValueError:
        side1 = 'ValErr_s1'
    
    try:
        side2 = float(side2)
    except ValueError:
        side2 = 'ValErr_s2'
    
    try:
        side3 = float(side3)
    except ValueError:
        side3 = 'ValErr_s3'
    
    if side1 == 'ValErr_s1' and side2 == 'ValErr_s2' and side3 == 'ValErr_s3':
        return 'ValErr', side1, side2, side3
    elif side1 == 'ValErr_s1' and side2 == 'ValErr_s2':
        return 'ValErr_s1s2', side1, side2, side3
    elif side1 == 'ValErr_s1' and side3 == 'ValErr_s3':
        return 'ValErr_s1s3', side1, side2, side3
    elif side2 == 'ValErr_s2' and side3 == 'ValErr_s3':
        return 'ValErr_s2s3', side1, side2, side3
    elif side1 == 'ValErr_s1' or side2 == 'ValErr_s2' or side3 == 'ValErr_s3':
        return None, side1, side2, side3
    else:
        perimeter = f'{side1 + side2 + side3:.2f}'
        return perimeter, side1, side2, side3