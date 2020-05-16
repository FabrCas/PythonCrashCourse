# per utilizzare gli input dati dall'utente si utilizza la funzione input(), che mette in
# pausa il programma e salva l'input in una variabile assegnata, prende come argomento la stringa
# da mostrare in console prima dello stop per la cattura dell'input

# messaggio = input("inserisci messaggio: ")
# print(messaggio)

# messaggioPrompt = "ciao\n"
# messaggioPrompt += "dicci il tuo nome: "
#
# nome = input(messaggioPrompt)
#
# print(nome)

# per prendere in input valori numerici si usa la funzione int(), analogo a str() con le stringhe

# promptMessage = "What's your favorite number?"
# numero = int(input(promptMessage))
# if numero>=50 and numero<=100:
#   print("e' un numero maggiore di 50")
# elif numero>=100:
#   print("e' un numero maggiore di 100")
# else:
#   print("e' un numero minore di 50")
#
# % viene utilizzato per effettuare il modulo base n di un certo numero
#
# if numero%2==0:
#   print("il numero è paro")
# else:
#   print("il numero e' disparo")

# introduzione al ciclio while in python, esempio incremento unitario numero fino a 5

#number = 0
# while number <= 5:
#    print(number)
#    number += 1
#

# terminazione del ciclo in base all'input dell'utente

# message = "nulla"
# while message != "esci":
#     message = input("inserisci una stringa, 'esci' per uscire:  ")
#     if message == "esci":
#         print("uscita in corso...")
#     else:
#         print("input: " + message)

# esempio precedente con l'utilizzo di Flag

# active = True
# while active:
#    message = input("insersci stringa: ")
#    if message == "esci":
#        print("uscita in corso...")
#        active = False
#    else:
#        print("input: " + message)
#
# message= ""
#

# vediamo ora l'utilizzo della parole chiave break per uscire dal loop

# while True:
#    message = input("insersci stringa: ")
#    if message == "esci":
#        print("uscita in corso...")
#        break
#    else:
#        print("input: " + message)
#

# vediamo ora l'utilizzo della parola chiave continue, per ritornare all'inizio del loop
# continue svolge l'operazione di break unicamente per quella iterazione
# immaginiamo di voler stampare unicamente i valori dispari


#counter = 0
# while counter < 10:
#    counter += 1
#    if counter % 2 == 0:
#        continue  # non svolgere le altre istruzioni del ciclo
#    print(counter)
#

# loop while con liste e dizionari

#utentiDaProcessare = ["Luisa", "Mario", "Antonio"]
#utentiProcessati = []
#
# while utentiDaProcessare:
#    utente = utentiDaProcessare.pop()
#    print("Processo per l'utente " + utente + " in corso ...")
#    utentiProcessati.append(utente)
#
# for user in utentiProcessati:
#    print("l'utente " + user + " e' stato processato")
#


# altro esempio, pensiamo di eliminare tutte le istanze di un elemento da una lista
# number=[1,2,3,3,3,6,7,2,3,7,1,1,78,100,3]
#
# while 3 in number:
#    number.remove(3)
# print(number)


# esempio in cui si riempe un dizionario con gli input dell'utente

inserimentoAttivo = True
dizionario = {}

while inserimentoAttivo:
    key = input(
        "inserisci la chiave da mettere nel dizionario: [digita esci per terminare]\n")
    if key.strip() == 'esci':
        inserimentoAttivo = False
    else:
        value = input("inserisci il valore per la chiave: [" +
                      key + "] del dizionario: \n")
        dizionario[key.strip()] = value.strip()
print(dizionario)
g