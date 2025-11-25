import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = circle_area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_positive(self):
        res = circle_area(3)
        self.assertAlmostEqual(res, math.pi * 9)

    def test_perimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        res = circle_perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_positive(self):
        res = circle_perimeter(5)
        self.assertAlmostEqual(res, 10 * math.pi)