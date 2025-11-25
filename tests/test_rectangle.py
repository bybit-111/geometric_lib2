import unittest
import math

from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = rectangle_area(4, 5)
        self.assertEqual(res, 20)

    def test_perimeter_zero(self):
        res = rectangle_perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = rectangle_perimeter(3, 4)
        self.assertEqual(res, 14)
