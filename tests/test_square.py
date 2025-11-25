import unittest
import math

from square import area as square_area, perimeter as square_perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = square_area(5)
        self.assertEqual(res, 25)

    def test_perimeter_zero(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = square_perimeter(3)
        self.assertEqual(res, 12)