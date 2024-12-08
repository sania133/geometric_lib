import unittest
from calculate import calc

class TestCalculate(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(calc('circle', 'area', 5), 78.53981633974483)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(calc('circle', 'perimeter', 5), 31.41592653589793)

    def test_square_area(self):
        self.assertEqual(calc('square', 'area', 4), 16)

    def test_square_perimeter(self):
        self.assertEqual(calc('square', 'perimeter', 4), 16)

    def test_triangle_area(self):
        self.assertAlmostEqual(calc('triangle', 'area', 3, 4, 5), 6.0)

    def test_triangle_perimeter(self):
        self.assertEqual(calc('triangle', 'perimeter', 3, 4, 5), 12)

    def test_invalid_shape(self):
        with self.assertRaises(ValueError):
            calc('hexagon', 'area', 5)

    def test_neg_size_area_circle(self):
        with self.assertRaises(ValueError):
            calc('circle', 'area', -1)

    def test_neg_size_area_square(self):
        with self.assertRaises(ValueError):
            calc('square', 'area', -1)

    def test_neg_size_area_triangle(self):
        with self.assertRaises(ValueError):
            calc('triangle', 'area', -3, 4, 5)  # Тестируем на одной отрицательной стороне

if __name__ == '__main__':
    unittest.main()
