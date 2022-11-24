from math import pi

def circ_area():
    r = float(input('Circle radius: ').strip())
    A = f'{pi * r ** 2:.2f}'
    
    return A

def rect_area():
    l = float(input('Rectangle length: ').strip())
    w = float(input('Rectangle width: ').strip())
    A = f'{l * w:.2f}'
    
    return A

def square_area():
    s = float(input('Square length: ').strip())
    A = f'{s ** 2:.2f}'
    
    return A

def tri_area():
    b = float(input('Triangle base: ').strip())
    h = float(input('Triangle height: ').strip())
    A = f'{0.5 * b * h:.2f}'
    
    return A