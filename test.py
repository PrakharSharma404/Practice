import unittest
from main import square_root, factorial, natural_log, power
import math

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(-1), "Square root of a negative number is not defined in real numbers.")

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(-3), "Factorial is not defined for negative numbers.")

    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(1), 0, places=5)
        self.assertAlmostEqual(natural_log(math.e), 1, places=5)
        self.assertEqual(natural_log(-1), "Natural logarithm is not defined for zero or negative numbers.")
        self.assertEqual(natural_log(0), "Natural logarithm is not defined for zero or negative numbers.")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -2), 0.25)

if __name__ == "__main__":
    unittest.main()
