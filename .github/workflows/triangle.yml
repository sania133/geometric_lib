import unittest
import triangle

class TestTriangle(unittest.TestCase):
    def test_triangle_area_positive(self):
        # Arrange
        sides = (3, 4, 5)
        expected_area = 6

        # Act
        result = triangle.calculate_area(*sides)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=2)

    def test_triangle_perimeter_positive(self):
        # Arrange
        sides = (3, 4, 5)
        expected_perimeter = 12

        # Act
        result = triangle.calculate_perimeter(*sides)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_triangle_invalid_sides(self):
        # Arrange
        sides = (1, 2, 10)

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.calculate_area(*sides)

        with self.assertRaises(ValueError):
            triangle.calculate_perimeter(*sides)
