import unittest
import square

class TestSquare(unittest.TestCase):
    def test_square_area_positive(self):
        # Arrange
        side = 4
        expected_area = 16

        # Act
        result = square.calculate_area(side)

        # Assert
        self.assertEqual(result, expected_area)

    def test_square_perimeter_positive(self):
        # Arrange
        side = 5
        expected_perimeter = 20

        # Act
        result = square.calculate_perimeter(side)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_square_negative_side(self):
        # Arrange
        side = -4

        # Act & Assert
        with self.assertRaises(ValueError):
            square.calculate_area(side)

        with self.assertRaises(ValueError):
            square.calculate_perimeter(side)
