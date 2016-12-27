from decimal import Decimal
import decimal
from physics import Vector, Body

decimal.getcontext().prec = 3

def main():
    elements = [
        Body(1, (1,2,3)), Body(2, (2,-3,4))
    ]

    for point_mass in elements:
        print(point_mass)
        print('weight: {}'.format(point_mass.weight))

    total_mass = Decimal(0)
    for point_mass in elements:
        total_mass += point_mass.mass

    first_moment = sum([body.first_moment for body in elements], Vector())
    combined_center = first_moment / total_mass
    print('Combined Center of Gravity: {}'.format(combined_center))

if __name__ == '__main__':
    main()
