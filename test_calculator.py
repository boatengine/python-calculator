import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)


    def test_sub(self):
        self.assertEqual(self.calc.subtract(5,2),3)

    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(2,3),-1)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(3,7),21)

    def test_mul_nenative(self):
        self.assertEqual(self.calc.multiply(7,-3),-21)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,5),2)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(10,-5),-2)


    def test_mod(self):
        self.assertEqual(self.calc.modulo(10,3),1)

    def test_mod_negative(self):
        self.assertEqual(self.calc.modulo(-10,2),0)
    # def test_
if __name__ == '__main__':
    unittest.main()