from decimal import Decimal
from math import cos
import collections

from physics import Vector

G = 9.8

Measurement = collections.namedtuple('Measurement', ['width', 'height', 'length'])
Angle = collections.namedtuple('Angle', ['x', 'y', 'z'])

class Target:
    def __init__(self, measurement, position):
        self.measurement = Measurement(*measurement)
        self.position = Vector(*position)
        self._get_coordinates()

    def __str__(self):
        return '{} at {}'.format(self.measurement, self.position)

    def _get_coordinates(self):
        x, y, z = self.position
        w, h, l = self.measurement
        x0, x1 = x - Decimal(w/2), x + Decimal(w/2)
        y0, y1 = y - Decimal(h/2), y + Decimal(h/2)
        z0, z1 = z - Decimal(l/2), z + Decimal(l/2)

        self.coords = ((x0, x1), (y0, y1), (z0, z1))
        return self.coords

    def isContact(self, position):
        xx = self.coords[0]
        yy = self.coords[1]
        zz = self.coords[2]

        projectile = Vector(*position)

        xin = True if xx[0] <= projectile.x <= xx[1] else False
        yin = True if yy[0] <= projectile.y <= yy[1] else False
        zin = True if zz[0] <= projectile.z <= zz[1] else False

        return xin and yin and zin

class Projectile:
    def __init__(self, v0, angle, position):
        self.v0 = v0
        self.angle = Angle(*angle)
        self.position = Vector(*position)

    def __iter__(self):
        time = 0
        while True:
            yield self.get_position(time)
            time += 0.1

    def get_position(self, time):
        v0 = self.v0
        sx = v0*cos(self.angle.x) * time
        sy = v0*cos(self.angle.y) * time + (-G) * time**2 / 2
        sz = v0*cos(self.angle.z) * time
        return (sx,sy,sz)

def do_sim():
    target = Target((2,2,2), (500, 400, -300))
    print('타겟: {}'.format(str(target)))

    v_init = input('Initial Velocity (m/s): ')
    projectile = Projectile(v_init, (0,0,0), (10,10,10))
    for x,y,z in projectile:
        print('({:.2f}, {:.2f}, {:.2f})'.format(x,y,z))
        if not y > 0 and x > 0:
            return print('Hit ground')
        # check if projectile hit target
        hit = target.isContact((x,y,z))
        if hit:
            return print('Hit' if hit else 'Miss')

if __name__ == '__main__':
    do_sim()
