import unittest

VALID_NUMBER = '601234567'
VALID_WITH_PLUS = '+48{}'.format(VALID_NUMBER)
VALID_WITH_ZEROES = '00{}'.format(VALID_WITH_PLUS[1:])


class PhoneNumbersTests(unittest.TestCase):

    def testFoo(self):
        self.failUnless(False)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
