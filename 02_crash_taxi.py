from decimal import Decimal
import decimal

# decimal.getcontext().prec = 3
G = Decimal(9.81)

from physics import Vector, Body

class RectCylinder:
    def __init__(self, body, a=0, b=0, l=0):
        self.body = body
        self.a = Decimal(a)
        self.b = Decimal(b)
        self.l = Decimal(l)

    def moment_inertia(self, center_gravity=None):
        I_xx = (self.body.mass / 12) * (self.a**2 + self.l**2) if self.a and self.l else 0
        I_yy = (self.body.mass / 12) * (self.b**2 + self.l**2) if self.b and self.l else 0
        I_zz = (self.body.mass / 12) * (self.a**2 + self.b**2) if self.a and self.b else 0

        # parallel axis theorem
        if center_gravity:
            mass = self.body.mass
            position = self.body.position

            d2_xx = (position.y - center_gravity.y)**2 + (position.z - center_gravity.z)**2
            d2_yy = (position.x - center_gravity.x)**2 + (position.z - center_gravity.z)**2
            d2_zz = (position.x - center_gravity.x)**2 + (position.y - center_gravity.y)**2

            I_xx += mass * d2_xx if I_xx else 0
            I_yy += mass * d2_yy if I_yy else 0
            I_zz += mass * d2_zz if I_zz else 0

        return I_xx + I_yy + I_zz

def main():
    car = Body(17500/G, (30.5, 30.5))
    driver = Body(850/G, (31.5, 31))
    fuel = Body(993/G, (28, 30.5))

    total_mass = sum([car.mass, driver.mass, fuel.mass])
    total_weight = sum([car.weight, driver.weight, fuel.weight])
    print('총 질량 (무게):\t{:.1f} kg ({:.1f} N)'.format(total_mass, total_weight))

    center_gravity = sum(
        [car.first_moment, driver.first_moment, fuel.first_moment], Vector())
    center_gravity /= total_mass
    print('질량 중심 (x, y):\t{}'.format(center_gravity))

    model={}
    model['car'] = RectCylinder(car, 1.80, 4.70)
    model['driver'] = RectCylinder(driver, 0.5, 0.9)
    model['fuel'] = RectCylinder(fuel, 0.9, 0.5)

    total_moment_inertia = Decimal(0)
    for name, model in model.items():
        mass_element_inertia = model.moment_inertia(center_gravity)
        total_moment_inertia += mass_element_inertia
        print('\t{}: {:.1f} '.format(name, mass_element_inertia))

    print('관성 모멘트:\t{:.2f}'.format(total_moment_inertia))

if __name__ == '__main__':
    main()
