#Leggere da un file
filename="piGreco.txt"
#open(nomefile,  modalità di apertura), se la modalità di apertura non è specificata, si intende la lettura
with open(filename) as file_object:
	contents=file_object.read()
	print(contents)
# Python chiudera automaticamente il file quando non servirà più, senza che effettuiamo la chiamata close()

#leggere linea dopo linea
print("\n*******************\n")
with open(filename) as file_object:
	for line in file_object:
		print(line)
#spazi biachi dovuti al carattere per andare a capo nel file di testo
print("\n*******************\n")
#per risolvere:
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

print("\n*******************\n")

#costruire una lista contenente le righe del file

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line)
#Quando Python legge da un file interpreta tutto come una stringa

#is your birthdate contained in PI?
# print("verifichiamo se il tuo compleanno e' contenuto nel PI greco...")
# with open(filename) as file_object:
# 	piStringa=""
# 	lines= file_object.readlines()
# 	for line in lines:
# 		piStringa += line.rstrip()
# 
# 	birthdate= input("Inserisci il tuo compleanno nella forma ddmmyy: ")
# 	if birthdate in piStringa:
# 		print("e' contenuto")
# 	else:
# 		print("non e' contenuto")


#scrivere su un file


filename= "scrivimi.txt"

with open(filename,'w') as file_object:  #va bene anche la modalita' r+
	file_object.write("scrivo su scrivimi.txt ")

#per appendere una stringa al file desiderata si deve usare la modalità a

#Eccezioni
print("*********************Exception*****************")

#catturiamo le eccezioni con i blocchi try except

try:
	print(5/0)
except ZeroDivisionError:
	print("\nstai tentando di dividere un numero con zero!\n")

#esempio dell'uso delle eccezioni per evitare crash
#
#print("semplice calcolatrice che divide due numeri: ")
#while True:
#	numberOne = input("inserisci il primo numero, oppure 'q' per uscire: ")
#	if (numberOne=='q'):
#		print("terminazione programma")
#		break
#	elif (not numberOne.isnumeric()):
#		print("hai inserito valori non numerici")
#		continue
#	
#	numberTwo= input("inserisci il secondo numero, oppure 'q' per uscire: ")
#	if (numberTwo=='q'):
#		print("terminazione programma")
#		break
#	elif (not numberTwo.isnumeric()):
#		print("hai inserito valori non numerici")
#		continue
#	try:
#		result= int(numberOne)/int(numberTwo)
#		print("il risutato e' " + str(result))
#	except ZeroDivisionError:
#		print("Attenzione, hai cercato di dividere un numero con 0!")

# oppure tramite l'utiizzo dell'else dopo la cattura

#	try:
#		result= int(numberOne)/int(numberTwo)
#	except ZeroDivisionError:
#		print("Attenzione, hai cercato di dividere un numero con 0!")
#	else:
#		print("il risutato e' " + str(result))


	
# gestire il FileNotFoundException
filename= "alice.txt"
try:
	with open(filename) as oggettoFile:
		testo= oggettoFile.read()
		print(testo)
except FileNotFoundError:
	print("file non trovato per il path: "+ filename )


# funzione che conta il numero di parole all'interno di un file di testo

def numberWords(filename):
	try:
		with open(filename) as file_o:
			contenuto= file_o.read()
	except FileNotFoundError:
		print("Il file desiderato non e' raggiungibile")
	else:
		
		counter= len(contenuto.split())
		print("il file contiene "+ str(counter) + " parole!")

file= "scrivimii.txt"
numberWords(file)

# possiamo anche non per forza mettere a conosceneza l'utente del fatto che un file
# non sia disponibile, rendendo "silenziosa" un exception e quindi un fallimento dovuto a qualcosa

def numberWords(filename):
	try:
		with open(filename) as file_o:
			contenuto= file_o.read()
	except FileNotFoundError:
		pass   #questo statement è utile a ricondarci che qui abbiamo ignorato una possibile azione per gestire un Exception
	else:
		
		counter= len(contenuto.split())
		print("il file contiene "+ str(counter) + " parole!")
	
file= "scrivimii.txt"
numberWords(file)

print("\n******Gestione dati da salvare attraverso il formato JSON*******\n")

#json.dump() salvare dati
#json.load() caricare i dati

import json

numeri =[1,2,3,4,5,6]

with open("numbers.json",'w') as json_ob:
	json.dump(numeri, json_ob)


with open("numbers.json") as json_ob:
	print(json.load(json_ob))


""" Questo rappresenta una DocString e non è un commento, utile per definire lo scopo di funzioni, classi, ecc."""
# in Python il valore nullo è dato con la parola chiave None
print(None)

