# Part 1
# Import the necessary modules
from shapes.area import *
from shapes.perimeter import *


def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')

    # Code to check that a valid shape has been selected
    shape = int(input('Shape number: ').strip())
    while shape < 1 or shape > 4:
        shape = int(input('Shape number (1-4): ').strip())

    return shape


def main():
    while True:
        shape = selection()
        comp = int(input('Computation (Area = 1 or Perimeter = 2): ').strip())
        while comp < 1 or comp > 2:
            comp = int(input('Enter 1 or 2: ').strip())
        
        if comp == 1:
            if shape == 1:
                circle_a = circ_area()
                print('Circle area =', circle_a)
            elif shape == 2:
                rectangle_a = rect_area()
                print('Rectangle area =', rectangle_a)
            elif shape == 3:
                square_a = square_area()
                print('Square area =', square_a)
            else:
                triangle_a = tri_area()
                print('Triangle area =', triangle_a)
        else:
            if shape == 1:
                circle_c = circ_circumference()
                print('Circle circumference =', circle_c)
            elif shape == 2:
                rectangle_p = rect_perimeter()
                print('Rectangle perimeter =', rectangle_p)
            elif shape == 3:
                square_p = square_perimeter()
                print('Square perimeter =', square_p)
            else:
                triangle_p = tri_perimeter()
                print('Triangle perimeter =', triangle_p)

        cont = input('Continue (y/n): ').strip().lower()
        while cont != 'y' and cont != 'n':
            cont = input('Enter y or n: ').strip().lower()
        
        if cont == 'y':
            continue
        else:
            print('PROGRAM DONE')
            break

if __name__ == '__main__':
    main()
