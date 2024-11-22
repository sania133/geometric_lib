import unittest
import circle

class TestCircle(unittest.TestCase):
    def test_circle_area_positive(self):
        # Arrange
        radius = 5
        expected_area = 78.539816  # π * r^2

        # Act
        result = circle.calculate_area(radius)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=6)

    def test_circle_perimeter_positive(self):
        # Arrange
        radius = 7
        expected_perimeter = 43.982297  # 2 * π * r

        # Act
        result = circle.calculate_perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected_perimeter, places=6)

    def test_circle_zero_radius(self):
        # Arrange
        radius = 0
        expected_area = 0
        expected_perimeter = 0

        # Act
        area_result = circle.calculate_area(radius)
        perimeter_result = circle.calculate_perimeter(radius)

        # Assert
        self.assertEqual(area_result, expected_area)
        self.assertEqual(perimeter_result, expected_perimeter)

    def test_circle_negative_radius(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            circle.calculate_area(radius)

        with self.assertRaises(ValueError):
            circle.calculate_perimeter(radius)
