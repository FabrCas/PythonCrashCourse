# utilizzo del loop for, molto simile al foreach di Java
nomi = ["Alberto", "Luisa", "Gianni"]
for nome in nomi:
    print(nome.lower())
# python l'indentazione come carattere per la interconnessione del codice, analogo utilizzo di ; in C
# la funzione range() di python permette di creare una array con valori numerici racchiusi in un certo range,
# primo estremo incluso mentre il secondo no
for val in range(1, 101):
    print(val)
# possiamo dare un altro valore alla funzione range() per indicargli l'incremento dei valori desiderati nel range
print("\n")
print("valori pari fino a 100")
for val in range(2, 101, 2):
    print(val)
# possiamo salvare i valori forniti dalla funzione range() direttamente in una lista
print("\n")
num = list(range(1, 101))
print(num)
# 3 funzioni di python per il max, il min e la somma
print("max")
print(max(num))
print("min")
print(min(num))
print("sum")
print(sum(num))


squares = []
for value in range(1, 6):
    squares.append(value**2)
print(squares)
# list comprehensions, concisa ma poco legibile
squares2 = [value**2 for value in range(1, 6)]
print(squares2)

# in python è possibile lavorare con alcune parti di una lista
print("\n")
print(squares2[2:4])
print(squares2[:4])
print(squares2[3:])


num = ["1", "2", "3"]
num2 = num[:]
num.append("4")
num2.append("5")
print(num)
print(num2)

print("\n*******************tuple*****************************\n")
# definzione e utilizzo delle tuple
# da notare la inizializzazione con parentesi tonde, invece di quelle quadrate (array)
dimensioni = (100, 20)
print(dimensioni[0])
print(dimensioni[1])
# dimensioni[0] = 345 ->errore, è impossibile modificare il contenuto di una tupla, è possibile però fare la dichiarazione di una nuova nella stessa variabile
dimensioni = (300, 100)
for dim in dimensioni:
    print(dim)
