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
            suma_cyfr_liczby(12.34)
        with self.assertRaises(TypeError):
            suma_cyfr_liczby(None)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            suma_cyfr_liczby(-123)

class TestSrednia(unittest.TestCase):
    def test_srednia(self):
        self.assertAlmostEqual(srednia([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(srednia([10, 20, 30]), 20.0)
        self.assertAlmostEqual(srednia([-1, 1]), 0.0)
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            srednia([])
            raise ValueError("Lista nie może być pusta.")
            
    def test_type_error(self):
        with self.assertRaises(TypeError):
            srednia("ciąg tekstowy")
        with self.assertRaises(TypeError):
            srednia(None)
        with self.assertRaises(TypeError):
            srednia((1,2,3))
            
if __name__ == '__main__':
    unittest.main()