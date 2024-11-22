import unittest
from calculate import calc

class TestCalculate(unittest.TestCase):
    def test_calculate_circle_area(self):
        # Arrange
        fig = 'circle'
        func = 'area'
        size = [7]
        expected_result = 153.938040

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected_result, places=6)

    def test_calculate_square_perimeter(self):
        # Arrange
        fig = 'square'
        func = 'perimeter'
        size = [5]
        expected_result = 20

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calculate_triangle_area(self):
        # Arrange
        fig = 'triangle'
        func = 'area'
        size = [3, 4, 5]
        expected_result = 6

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_invalid_figure(self):
        # Arrange
        fig = 'hexagon'
        func = 'area'
        size = [6]

        # Act & Assert
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_function(self):
        # Arrange
        fig = 'circle'
        func = 'volume'
        size = [7]

        # Act & Assert
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_size_length(self):
        # Arrange
        fig = 'triangle'
        func = 'perimeter'
        size = [3, 4]  # Missing one side

        # Act & Assert
        with self.assertRaises(TypeError):
            calc(fig, func, size)
