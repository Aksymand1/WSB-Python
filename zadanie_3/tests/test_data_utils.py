
from ..my_awesome_lib.data_utils import usun_duplikaty, ListProcessor
import unittest

class TestDataUtils(unittest.TestCase):
    def test_usun_duplikaty(self):
        self.assertEqual(usun_duplikaty([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(usun_duplikaty([]), [])
        self.assertEqual(usun_duplikaty([1, 1, 1, 1]), [1])
        self.assertEqual(usun_duplikaty([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])
        self.assertEqual(usun_duplikaty(['a', 'b', 'a', 'c', 'c', 'd', 'a', 'm', 'b']), ['a', 'b', 'c', 'd', 'm'])
        
    def test_instance(self):
        self.assertIsInstance(usun_duplikaty([1,2,3]), list)
        self.assertIsInstance(usun_duplikaty((1,2,3)), list)
        self.assertIsInstance(usun_duplikaty([]), list)
        self.assertIsInstance(usun_duplikaty("ciąg tekstowy"), list)
        self.assertNotIsInstance(usun_duplikaty([1,2,3]), tuple)
        
    def test_type_error(self):
        self.assertRaises(TypeError, usun_duplikaty, None)
    
    def test_iterable_error(self):
        self.assertRaises(TypeError, usun_duplikaty, 12345)
        self.assertRaises(TypeError, usun_duplikaty, 12.345)

class TestListProcessor(unittest.TestCase):
    def test_list_processor(self):
        lp = ListProcessor()
        
        n = lp.losuj_n()
        self.assertTrue(10 <= n <= 100)
        
        generated_list = lp.generuj_liste(20)
        self.assertEqual(len(generated_list), 20)
        for num in generated_list:
            self.assertTrue(1 <= num <= 50)
        
        lp.data = [1, 2, 3, 4, 5]
        mapped_list = lp.mapuj()
        self.assertEqual(mapped_list, [-5, 0, -3, 0, -1])
        
        lp.data = [2, 4, 6]
        mapped_list = lp.mapuj()
        self.assertEqual(mapped_list, [0, 0, 0])
        
    def test_empty_data_map(self):
        lp = ListProcessor()
        lp.data = []
        mapped_list = lp.mapuj()
        self.assertEqual(mapped_list, [])
        
    def test_string_element_data_map(self):
        lp = ListProcessor()
        lp.data = [1, "two", 3]
        with self.assertRaises(TypeError):
            lp.mapuj()
            
    
if __name__ == '__main__':
    unittest.main()