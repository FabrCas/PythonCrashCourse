from unittest import TestCase
from testingCode import getFormattedName

class Test(TestCase):
    def test_get_formatted_name(self):

        name = getFormattedName("Giggino", "Bianchi")
        self.assertEqual(name, "Giggino Bianchi")