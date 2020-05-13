# definizione funzione

def hello_world(username):
    print("hello world " + username)


hello_world("Fabrizio")

# utilizzare keywords arguments, utile per non dover fare attenzione all'ordine degli argomenti e parametri


def gender_printer(man, woman):
    print(man + " e' un uomo")
    print(woman + " e' una donna")


# da notore l'ordine errato rispetto ad una normale chiamata con argomenti
gender_printer(woman="Annalisa", man="Mario")

# è possibile utilizzare dei valori di default per i parametri di una funzione,
# in modo da renderli opzionali
print("******************************************************************")


def gender_printer(man, woman="Luisa"):
    print(man + " e' un uomo")
    print(woman + " e' una donna")


gender_printer(man="Alessio", woman="Arianna")
gender_printer(man="Mirko")
gender_printer("Flavio")

print("******************************************************************")


# gestione valori di ritorno

def full_name_maker(firstName, secondName):
    return((firstName.strip() + " " + secondName.strip()).title())


print(full_name_maker("albert     ", "   einstein"))


print("******************************************************************")

# esempio con lista


def greet_users(users):
    while users:
        print("Hi user: " + users[0] + "!")
        # users.remove(user) attenzione!Non funzionerebbe a causa dello shifting automatico svolto da python
        # in questo modo leviamo sempre la l'elemento testa, e tutti gli altri elementi verranno spostati
        # di una posizione a sinistra, attenziona anche l'utilizzo del for avrebbe dato problemi a causa dello
        # shifting
        users.pop(0)


utenti = ["Luisa", "Alberto", "Giggi"]
greet_users(utenti)
print(utenti)


print("******************************************************************")

# prevenire che una funzione modifichi una lista, utilizzando una copia di una lista tramite la
# logica delle "slice"

utenti2 = ["Luigi", "Gianni"]
greet_users(utenti2[:])
print(utenti2)


# passare un valore arbitrario di parametri (*)
print("******************************************************************")
def greet_innumerableUsers(*users): #tupla vuota chiamata users
        print(str(users))
        for user in users:
            print("Hi user: " + str(user) + "!")

greet_innumerableUsers("franco", "gianni", "silvio", "lello")
#in realta' in questo caso abbiamo passato una tupla

#esempio in cui vengono mixati parametri posizionali e arbitrari

print("******************************************************************")
def greet_users2(owner,*users): #tupla vuota chiamata users
        print("owner: "+str(owner))
        for user in users:
            print("Hi user: " + str(user) + "!")

greet_users2("Gianni","Peppino","Franco")


#esempio per parametri arbitrari con keywords (**), passare valore e chiavi di un dizionario
print("******************************************************************")

def dictionaryMaker(title, author, **info):
    dictionary={}
    dictionary['title']=title
    dictionary['author']=author
    for k,v in info.items():
        dictionary[k]=v
    print(dictionary)


dictionaryMaker("Guida galattica per autostoppisti", "Douglas Adams", 
    page= 500, bookType= "sci-fi/humorous")

print("******************************************************************")

# una buona idea di programmazione è definire funzioni di uso comune in un modulo
# e importarle quando necessario tramite il comando: "import"

# import exModule
# 
# print(exModule.fattoriale(5))
# print(exModule.fattoriale(500))
# 

# e' possibile in alternativa importare una singola funzione da un modulo
# piuttosto che tutto il modulo, in questo caso cambia anche la chiamata alla funzione
# omettendo il nome del modulo:

# from exModule import fattoriale
# 
# print(fattoriale(6))
# 

# è possibile dare ad una funzione importata un alias

# from exModule import fattoriale as fatt
# print(fatt(6))# 

# è possibile anche dare un alis al modulo
# import exModule as fattMod

# è possibile inoltre importare singolarmente tutte le funzioni di un modulo 

from exModule import *

print(fattoriale(6))