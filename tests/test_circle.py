import unittest
import circle

class TestCircle(unittest.TestCase):
    def test_circle_area_positive(self):
        radius = 5
        expected_area = 78.539816  # π * r^2

        result = circle.area(radius)

        self.assertAlmostEqual(result, expected_area, places=6)

    def test_circle_perimeter_positive(self):
        radius = 7
        expected_perimeter = 43.982297  # 2 * π * r

        result = circle.perimeter(radius)

        self.assertAlmostEqual(result, expected_perimeter, places=6)

    def test_circle_zero_radius(self):
        radius = 0
        expected_area = 0
        expected_perimeter = 0

        area_result = circle.area(radius)
        perimeter_result = circle.perimeter(radius)

        self.assertEqual(area_result, expected_area)
        self.assertEqual(perimeter_result, expected_perimeter)

    def test_circle_negative_radius(self):
        radius = -5

        with self.assertRaises(ValueError):
            circle.area(radius)

        with self.assertRaises(ValueError):
            circle.perimeter(radius)
