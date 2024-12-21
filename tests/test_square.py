import unittest
import square


class TestSquare(unittest.TestCase):
    def test_square_area_positive(self):
        side = 4
        expected_area = 16

        result = square.area(side)

        self.assertEqual(result, expected_area)

    def test_square_perimeter_positive(self):
        side = 5
        expected_perimeter = 20

        result = square.perimeter(side)

        self.assertEqual(result, expected_perimeter)

    def test_square_negative_side(self):
        side = -4

        with self.assertRaises(ValueError):
            square.area(side)

        with self.assertRaises(ValueError):
            square.perimeter(side)


if __name__ == '__main__':
    unittest.main()
