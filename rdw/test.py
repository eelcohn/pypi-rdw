import unittest

from rdw import Rdw


class RdwTestCase(unittest.TestCase):

    def setUp(self):
        self.license_number = LicenseNumber('a-a88a-a ')

    def test_stripped(self):
        self.assertEqual(self.license_number.stripped, 'AA88AA')

    def test_formatted(self):
        self.assertEqual(self.license_number.formatted, 'AA-88-AA')


if __name__ == '__main__':
    unittest.main()
