import unittest
import triangle

class TestTriangle(unittest.TestCase):
    def test_triangle_area_positive(self):
        sides = (3, 4, 5)
        expected_area = 6

        result = triangle.area(*sides)

        self.assertAlmostEqual(result, expected_area, places=2)

    def test_triangle_perimeter_positive(self):
        sides = (3, 4, 5)
        expected_perimeter = 12

        result = triangle.perimeter(*sides)

        self.assertEqual(result, expected_perimeter)

    def test_triangle_invalid_sides(self):
        sides = (1, 2, 10)

        with self.assertRaises(ValueError):
            triangle.area(*sides)

        with self.assertRaises(ValueError):
            triangle.perimeter(*sides)
