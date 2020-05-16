print(__name__) #__main__ poichè è in esecuzione

# definizione di una classe 





class Dog:
	def __init__(self,name,age):   #metodo costruttore speciale che python utilizza automaticamente quando si crea
		self.name= name            #una nuova istanza di una certa classe
		self.age=age               #quindi noi scriviamo: Dog() -> successivamente python chiama __init__()

		self.id= 0             #settaggio di un valore di default per un attributo,
		                       #che potrà essere modificato dirattamente sull'istanza

# ogni metodo associato con una classe, automaticamente passera' l'argomento 'self'
# che contiene l'istanza di se stesso (la classe creata), in modo da poter accedere ai suoi attributi
# analogia con l'uso di this, senza la definzioni attributi utilizzato ad esempio in Java

	def sit(self):    
		print(self.name.title() + " is now sitting")

	def roll_over(self):
		print(self.name.title() + " is rolled over!")

	def setId(self, newID):
		self.id= newID
		print("ID has been updated")

	def defineMySelf(self):
		print("i'm a dog and my name is " + self.name)

	def setOwner(self, owner):
		self.owner=owner







#istanziamento di un oggetto della classe Dog e utilizzo di alcuni metodi
cane= Dog("Max", 3)
cane.sit()
cane.roll_over()

# possiamo accedere direttamente agli attributi di un oggetto
print(cane.id)
#modifica valore attributo
cane.id= 999  # tramite accesso diretto
print(cane.id)
cane.setId(99) # tramite metodo interno alla classe
print(cane.id)

print("***********print ereditarietà********************")
#ereditarietà di una classe, superclasse e sottoclasse
#sottoclasse: Pincher()
#superclasse: Dog()

class Pincher(Dog):
	def __init__(self, name, age, plutoniumDiet):
		"""inizilizzazione attributi del costruttore della superclasse"""
		super().__init__(name,age)  #in Python 2.7: super(Pincher, self).__init__(name,age)
		self.plutoniumDiet= plutoniumDiet

	def describePlutoniumDiet(self):   #nuovo metodo della superclasse
		print(self.name.title()+" eat every day " + str(self.plutoniumDiet)+ "g of Plutonium")

	#overriding di un metodo della classe madre
	def defineMySelf(self):
		print("i'm a Pincher and my name is " + self.name)


myDog= Pincher("Milo",9, 50)
myDog.sit()
myDog.describePlutoniumDiet()
cane.defineMySelf()
myDog.defineMySelf()

#attributi istanza

class Person():

	def __init__(self, name, age, gender):
		self.name=name
		self.age=age
		self.gender=gender
		self.animals=[]

	def description(self, dog):
		print("Hi my name is" +self.name+", and i'm "+ str(self.age)+ " years old")

	def setDog(self, dog):
		self.animals.append(dog)

faber= Person("Fabrizio",22,"Male")
faber.setDog(myDog)
faber.setDog(cane)
myDog.setOwner(faber)
print(faber.animals)

#importare una classe
from classeProva import test
test= test("import")

# è possibile definire quando classi di vogliano sullo stesso modulo (file)
# ma è sempre consigliabile definirne su diversi moduli ad eccezione di casi
# in cui le classi sono strettamente legate e ci sono motifazioni valide per operare in questa maniera

#importare piu' classi
from classeProva import test, test2
test= test("import")
test2= test2("import2")

# in alternativa è possibile caricare interi moduli importando ogni tipo di elemento che contiene
# quindi classi, funzioni, variabili, ecc.
import classeProva

test= classeProva.test("import")


# importare tutte le classi da un modulo senza dover utilizzare il modulo per utilizzare gli elementi importati
# (sconsigliato, a causa delle poca chiarezza sugli elementi effettivamente in utilizzo e della conflittualità possibile con
# alcuni nomi in utilizzo nel file in utilizzo)
from classeProva import *


# ovviamente le operazioni di import valgono anche per i stessi moduli, che ne possono fare tranquillamente utilizzo

# la python standard library è un insieme di moduli inclusi in ogni versione di python contenente elementi di utilità generali

from collections import OrderedDict

favoriteLanguages = OrderedDict()

favoriteLanguages['faber'] = 'Java'
favoriteLanguages['Ale'] = "C"
favoriteLanguages['Manu'] = 'Lua'

for name,language in favoriteLanguages.items():
	print(language+ " is the best for: " + name )