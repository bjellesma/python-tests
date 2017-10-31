import unittest
import calc

class TestCalc(unittest.TestCase):
    #NOTE test_(method name) is required
    #NOTE testing modules are run like "python -m unittest test_calc"
    #NOTE you can also use if __name__ == '__main__' to automate the cmd
    def test_add(self):
        self.assertEqual(result = calc.add(10, 5), 15)
        self.assertEqual(result = calc.add(-1, 1), 0)
        self.assertEqual(result = calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(result = calc.subtract(10, 5), 5)
        self.assertEqual(result = calc.subtract(-1, 1), -2)
        self.assertEqual(result = calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(result = calc.multiply(10, 5), 50)
        self.assertEqual(result = calc.multiply(-1, 1), -1)
        self.assertEqual(result = calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(result = calc.divide(10, 5), 2)
        self.assertEqual(result = calc.divide(-1, 1), -1)
        self.assertEqual(result = calc.divide(-1, -1), 1)

        self.assertRaises(ValueError, calc.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
