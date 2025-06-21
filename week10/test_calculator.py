import unittest
import math
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 0), 0)
    def test_divide(self):
        self.assertEqual(calculator.divide(6, 2), 3)
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(4, 0)
    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
    def test_root(self):
        self.assertEqual(calculator.root(9, 2), 3)
    def test_root_negative_even(self):
        with self.assertRaises(ValueError):
            calculator.root(-8, 2)
    def test_sine(self):
        self.assertAlmostEqual(calculator.sine(0), 0)
    def test_cosine(self):
        self.assertAlmostEqual(calculator.cosine(0), 1)
    def test_tangent(self):
        self.assertAlmostEqual(calculator.tangent(0), 0)
    def test_tangent_large(self):
        self.assertTrue(abs(calculator.tangent(math.pi/2)) > 100000)

if __name__ == '__main__':
    unittest.main()
