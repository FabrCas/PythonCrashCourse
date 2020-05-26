from unittest import TestCase

from exModule import fattoriale


class Test(TestCase):
    def test_fattoriale(self):
        num= fattoriale(5)
        self.assertEqual(num, 120)
