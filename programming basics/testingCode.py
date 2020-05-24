def getFormattedName(first, last):
    fullName = first.strip() + ' ' + last.strip()
    return fullName.title()

    # print("digita 'q' per uscire ")
    # while True:
    # 	first=input("digita il nome: \n")
    # 	#if (first=='q'):
    # 		break
    # 	last= input("digita il congnome: \n")
    # 	if (last=='q'):
    # 		break
    # 	fullName= getFormattedName(first,last)
    # 	print("il nome completo e' " + fullName)

    # la classe test deve essere una sottoclasse di unittest.TestCase

from unittest import TestCase

class NamesTestCase(TestCase):
    def test_name(self):
        name = getFormattedName("Giggino", "Bianchi")
        self.assertEqual(name, "Giggino Bianchi")