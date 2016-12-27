import pytest
from math import sqrt

from physics import Vector

class TestVector:

    @pytest.fixture
    def vectors(self):
        v1 = Vector(1,2,3)
        v2 = Vector(2,3,4)
        return v1, v2

    def test_eq(self, vectors):
        v1, v2 = vectors
        assert v1 == v1

    def test_neg(self, vectors):
        v1, *_ = vectors
        assert -v1 == Vector(-1,-2,-3)

    def test_abs(self, vectors):
        v, *_ = vectors
        assert abs(v) == sqrt(1**2+2**2+3**2)
        assert abs(-v) == sqrt(1**2+2**2+3**2)

    def test_pow(self, vectors):
        v, *_ = vectors
        assert v**2 == Vector(v.x**2, v.y**2, v.z**2)
        assert (-v)**2 == Vector(v.x**2, v.y**2, v.z**2)

    def test_add(self, vectors):
        v1, v2 = vectors
        assert v1 + v2 == Vector(3, 5, 7)

    def teset_sub(self, vectors):
        v1, v2 = vectors
        assert v1 - v1 == Vector()

    def test_mul(self, vectors):
        v1, v2 = vectors
        assert v1 * v2 == Vector(2,6,12)
        assert v1 * 2 == Vector(2,4,6)
        assert 2 * v1 == Vector(2,4,6)

    def test_div(self, vectors):
        v, *_ = vectors
        assert Vector(2,4,6) / 2 == v
        with pytest.raises(TypeError):
            2 / Vector(2,4,6)

        # assert Vector(1.2, 2.2, 3.3) / 2 == Vector(1.2/2, 2.2/2, 3.3/2)

    @pytest.mark.skip('Not Implemented')
    def test_cross(self, vectors):
        v1, v2 = vectors
