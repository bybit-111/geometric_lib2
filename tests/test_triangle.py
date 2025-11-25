import unittest
import math

from triangle import area as triangle_area, perimeter as triangle_perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        res = triangle_area(0, 0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = triangle_area(6, 4)
        self.assertEqual(res, 12)

    def test_perimeter_zero(self):
        res = triangle_perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)