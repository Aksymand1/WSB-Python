import unittest
from app import validate_email
from app import convert_date_format
from app import insert_random_numbers


class TestValidateEmail(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.valid_emails = ["example-1@test.com", "user@domain.com", "prawidlowy.email@domain.com",
                                "nowy_test@domain.com", "mail.user@domena.com", "email-test@testowa.domena.com"]
        
        self.invalid_emails = ["invalid-email.com", "user@.com", "user@domain,com", "user-test@domain@pl.com", "user1@pl"]
    
    def test_valid_emails(self):
        for email in self.valid_emails:
            self.assertTrue(validate_email(email), f'Expected {email} to be valid')
            
    def test_invalid_emails(self):
        for email in self.invalid_emails:
            self.assertFalse(validate_email(email), f'Expected {email} to be invalid')


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
    
    def test_convert_date_format(self):
        for input_date, expected_output in self.test_cases.items():
            self.assertEqual(convert_date_format(input_date), expected_output)
    
    def test_invalid_date_format(self):
        invalid_dates = ["2023-12-25", "25.12/2023", "invalid-date", "33-12-2023"]
        for date_str in invalid_dates:
            self.assertEqual(convert_date_format(date_str), "Niepoprawny format daty")
            
            
class TestInsertRandomNumbers(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.lst = [0] * 20
        
    def test_insert_random_numbers(self):
        insert_random_numbers(self.lst)
        for num in self.lst:
            self.assertIn(num, range(0, 20), f'Liczba {num} jest poza zakresem 0-20')
        self.assertEqual(len(self.lst), 20, 'Lista powinna zawierać 20 elementów')
        self.assertNotIn(None, self.lst, 'Lista nie powinna zawierać wartości None po wstawieniu liczb')
        self.assertIsInstance(self.lst, list, 'Wynik powinien być listą')

if __name__ == '__main__':
    unittest.main()