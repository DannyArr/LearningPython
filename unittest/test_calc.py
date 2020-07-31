# Thanks to Corey Schafer
# https://www.youtube.com/watch?v=6tNS--WetLI
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Unit-Testing 

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), -0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        #self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):  # learn - context managers: https://www.youtube.com/watch?v=-aKFBoZpiqA
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()