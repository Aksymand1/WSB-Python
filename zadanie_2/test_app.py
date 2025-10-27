import unittest
from app import validate_email

class TestValidateEmail(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = ["example-1@test.com", "user@domain.com", "prawidlowy.email@domain.com",
          "nowy_test@domain.com", "mail.user@domena.com", "email-test@testowa.domena.com"]
        for email in valid_emails:
            self.assertTrue(validate_email(email), f'Expected {email} to be valid')
            
    def test_invalid_emails(self):
        invalid_emails = ["invalid-email", "user@.com", "user@domain..com", "user@domain,com"]
        for email in invalid_emails:
            self.assertFalse(validate_email(email), f'Expected {email} to be invalid')
            
if __name__ == '__main__':
    unittest.main()
