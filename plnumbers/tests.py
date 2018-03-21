import unittest
from plnumbers import PhoneNumber

VALID_NUMBER = '601234567'
VALID_WITH_PLUS = '+48{}'.format(VALID_NUMBER)
VALID_WITH_ZERO = '00{}'.format(VALID_WITH_PLUS[1:])


class PhoneNumbersTests(unittest.TestCase):

    def test_valid_number(self):
        number = PhoneNumber.parse(VALID_NUMBER)
        self.assertIsInstance(number, PhoneNumber)

    def test_too_long_number(self):
        number = '1' * (PhoneNumber._MAX_LENGTH+1)
        with self.assertRaises(ValueError):
            number = PhoneNumber.parse(number)

    def test_too_short_number(self):
        number = '1' * (PhoneNumber._MIN_LENGTH-1)
        with self.assertRaises(ValueError):
            number = PhoneNumber.parse(number)

    def test_valid_with_plus(self):
        number = PhoneNumber.parse(VALID_WITH_PLUS)
        self.assertIsInstance(number, PhoneNumber)
        self.assertTrue(number.leading_plus)
        self.assertFalse(number.leading_zero)

    def test_valid_with_zero(self):
        number = PhoneNumber.parse(VALID_WITH_ZERO)
        self.assertIsInstance(number, PhoneNumber)
        self.assertFalse(number.leading_plus)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
