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


class NamesTestCase(TestCase):
    def test_name(self):
        name = getFormattedName("Giggino", "Bianchi")
        self.assertEqual(name, "Giggino Bianchi")

    def test_name2(self):
        name = getFormattedName("Giggino  ", "Bianchi", "  sir.")
        self.assertEqual(name, "Giggino Sir. Bianchi")


# una semplice classe da testare, che gestisce una domande e N risposte a essa

class AnonymoyusSurvey():
    def __init__(self, question):
        self.question= question
        self.responses= ["Java","C"]

    def show_question(self):
        print(self.question)

    def store_response(self, response):
        self.responses.append(response)

    def show_result(self):
        print("Survey results:")
        for response in self.responses:
            print(response)

# varibili utilizzate nel testing


class TestQuestion(TestCase):

    # il metodo setUp viene sempre eseguito prima di ogni funzione che comincia con la parola "test"
    def setUp(self):

        self.nRisposte = 2
        self.ultimaRispota = ""

        question = "che linguaggio di programmazione preferisci?"
        self.survey = AnonymoyusSurvey(question)
        self.survey.show_question()
        print("inserire 'q' per terminare \n")
        while True:
            risposta = input("Liguaggio: ")
            if risposta != 'q':
                self.nRisposte = self.nRisposte + 1
                self.ultimaRispota = risposta
                self.survey.store_response(risposta)
            else:
                break

        print("riposte:\n")
        self.survey.show_result()


    def testNumeroRisposte(self):
        self.assertEqual(len(self.survey.responses), self.nRisposte)

    def testUltimaRisposta(self):
        if self.ultimaRispota == "":
            self.assertTrue(self.survey.responses==["Java","C"])
        else:
            self.assertIn(self.ultimaRispota, self.survey.responses)




