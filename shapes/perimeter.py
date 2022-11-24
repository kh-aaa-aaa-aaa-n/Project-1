from math import pi

def circ_circumference():
    r = float(input('Circle radius: ').strip())
    C = f'{2 * pi * r:.2f}'
    
    return C

def rect_perimeter():
    l = float(input('Rectangle length: ').strip())
    w = float(input('Rectangle width: ').strip())
    P = f'{l * 2 + w * 2:.2f}'
    
    return P

def square_perimeter():
    s = float(input('Square length: ').strip())
    P = f'{s * 4:.2f}'
    
    return P

def tri_perimeter():
    s1 = float(input('Triangle side 1: ').strip())
    s2 = float(input('Triangle side 2: ').strip())
    s3 = float(input('Triangle side 3: ').strip())
    P = f'{s1 + s2 + s3:.2f}'
    
    return P