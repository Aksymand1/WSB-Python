import unittest
from app import validate_email
from app import convert_date_format
from app import insert_random_numbers
from app import palindrom
from app import Sphere


class TestValidateEmail(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.valid_emails = ["example-1@test.com", "user@domain.com", "prawidlowy.email@domain.com",
                                "nowy_test@domain.com", "mail.user@domena.com", "email-test@testowa.domena.com"]
        
        self.invalid_emails = ["invalid-email.com", "user@.com", "user@domain,com", "user-test@domain@pl.com", "user1@pl"]
    
    def test_valid_emails(self):
        for email in self.valid_emails:
            self.assertTrue(validate_email(email), f'Podany email: {email} powinien być prawidłowy')
            
    def test_invalid_emails(self):
        for email in self.invalid_emails:
            self.assertFalse(validate_email(email), f'Podany email: {email} powinien być nieprawidłowy')
    
    #Test typu błędu dla niepoprawnych typów danych        
    def test_type_error(self):
        with self.assertRaises(TypeError):
            validate_email(12.34)
        with self.assertRaises(TypeError):
            validate_email(12345)
        with self.assertRaises(TypeError):
            validate_email(None)
        with self.assertRaises(TypeError):
            validate_email(["nie", "jestem", "emailem"])


class TestDateFormatConversion(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.test_cases = {
            "25-12-2023": "2023/12/25",
            "01-01-2020": "2020/01/01",
            "15-08-1945": "1945/08/15",
            "31.10.2021": "2021/10/31",
            "16.03.1998": "1998/03/16"
        }
        self.invalid_dates = ["2023-12-25", "25.12/2023", "invalid-date", "33-12-2023"]
        
    #Testowanie poprawnej konwersji dat
    def test_convert_date_format(self):
        for input_date, expected_output in self.test_cases.items():
            self.assertEqual(convert_date_format(input_date), expected_output)
    
    def test_invalid_date_format(self):
        for date_str in self.invalid_dates:
            self.assertEqual(convert_date_format(date_str), "Niepoprawny format daty")
            
            
class TestInsertRandomNumbers(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lst = [0] * 20
        
    def test_insert_random_numbers(self):
        insert_random_numbers(self.lst)
        for num in self.lst:
            self.assertIn(num, range(0, 21), f'Liczba {num} jest poza zakresem 0-20')
        self.assertEqual(len(self.lst), 20, 'Lista powinna zawierać 20 elementów')
        self.assertNotIn(None, self.lst, 'Lista nie powinna zawierać wartości None po wstawieniu liczb')
        self.assertIsInstance(self.lst, list, 'Wynik powinien być listą')


class TestPalindrome(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.palindromes = ["kajak", "level", "radar", "A to kanapa pana Kota", "racecar", "Kobyła ma mały bok"]
        self.non_palindromes = ["hello", "world", "python", "unittest", "example", "nie jestem palindromem"]
        # Zdefiniowanie przypadków testowych

    def test_palindromes(self):
        for word in self.palindromes:
            self.assertTrue(palindrom(word), f'Podane wyrażenie: {word} powinno być pralindromem')
            # Testowanie poprawnych palindromów
            
    def test_non_palindromes(self):
        for word in self.non_palindromes:
            self.assertFalse(palindrom(word), f'Podane wyrażenie: {word} nie powinno być pralindromem')
            # Testowanie wyrażeń, które nie są palindromami
            
    def test_empty_string(self):
        self.assertTrue(palindrom(""), 'Pusty ciąg znaków powinien być traktowany jako palindrom')
        #Testowanie pustego ciągu znaków jako palindromu

class TestSphereVolume(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.test_cases = {
            3: 113.09724,
            5.5: 696.90932,
            10: 4188.79067,
            0.25: 0.06545,
            7.8: 1991.14858
        }
        self.spheres = [Sphere(radius) for radius in self.test_cases.keys()]
        self.non_spheres = ["not a sphere", 123, [1,2,3], {'radius':5}]
        
    def test_sphere_volume(self):
        for radius, expected_volume in self.test_cases.items():
            calculated_volume = Sphere.sphere_volume(radius)
            self.assertAlmostEqual(calculated_volume, expected_volume, places=5,
                                   msg=f'Objętość kuli o promieniu {radius} powinna wynosić {expected_volume:.6f}, otrzymano {calculated_volume:.6f}')            
    
    #Testowanie czy obiekty są instancjami klasy Sphere
    def test_instance_type(self):
        for sphere in self.spheres:
            self.assertIsInstance(sphere, Sphere, 'Obiekt powinien być instancją klasy Sphere')
    
    def test_non_sphere_instances(self):
        for item in self.non_spheres:
            self.assertNotIsInstance(item, Sphere, 'Obiekt nie powinien być instancją klasy Sphere')
        

if __name__ == '__main__':
    unittest.main()