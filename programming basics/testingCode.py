from unittest import TestCase



def getFormattedName(first, last, middle= ""):
    if middle:
        fullName = first.strip() + ' ' + middle.strip() + ' ' + last.strip()
    else:
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

# una semplice classe da testare, che gestisce una domande e N risposte a essa

class AnonymoyusSurvey():
    def __init__(self, question):
        self.question= question
        self.responses= []

    def show_question(self):
        print(self.question)

    def store_response(self, response):
        self.responses.append(response)

    def show_result(self):
        print("Survey results:")
        for response in self.responses:
            print(response)


class NamesTestCase(TestCase):
    def test_name(self):
        name = getFormattedName("Giggino", "Bianchi")
        self.assertEqual(name, "Giggino Bianchi")

#test che fallirà
    def test_name2(self):
        name = getFormattedName("Giggino  ", "Bianchi", "  sir  .")
        self.assertEquals(name, "Giggino Sir. Bianchi")


