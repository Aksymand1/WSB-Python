from ..my_awesome_lib.math_tools import suma_cyfr_liczby, srednia, silnia, fibonacci
import unittest

class TestSumaCyfr(unittest.TestCase):
    def suma_cyfr(self):
        self.assertEqual(suma_cyfr_liczby(12345), 15)
        self.assertEqual(suma_cyfr_liczby(0), 0)
        self.assertEqual(suma_cyfr_liczby(999), 27)
        self.assertEqual(suma_cyfr_liczby(1001), 2)
    
    def test_type_error(self):
        with self.assertRaises(TypeError):
            suma_cyfr_liczby("12345")
        with self.assertRaises(TypeError):
            suma_cyfr_liczby(None)

class TestSrednia(unittest.TestCase):
    def test_srednia(self):
        self.assertAlmostEqual(srednia([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(srednia([10, 20, 30]), 20.0)
        self.assertAlmostEqual(srednia([-1, 1]), 0.0)
        
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            srednia([])
    
    def test_type_error(self):
        with self.assertRaises(TypeError):
            srednia("not a list")
        with self.assertRaises(TypeError):
            srednia([1, 2, "three"])

class TestSilnia(unittest.TestCase):
    def test_silnia(self):
        self.assertEqual(silnia(0), 1)
        self.assertEqual(silnia(1), 1)
        self.assertEqual(silnia(5), 120)
        self.assertEqual(silnia(10), 3628800)
    
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            silnia(-5)
    
    def test_type_error(self):
        with self.assertRaises(TypeError):
            silnia("5")
        with self.assertRaises(TypeError):
            silnia(None)
    
    def test_large_input(self):
        self.assertEqual(silnia(20), 2432902008176640000)

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), (1, 1))
        self.assertEqual(fibonacci(2), (7, 13))
        self.assertEqual(fibonacci(3), (12, 144))
        self.assertEqual(fibonacci(4), (17, 1597))
    
    def test_type_error(self):
        with self.assertRaises(TypeError):
            fibonacci("3")
        with self.assertRaises(TypeError):
            fibonacci(None)
    
    def test_zero_input(self):
        self.assertEqual(fibonacci(0), (1, 1))
    
if __name__ == '__main__':
    unittest.main()