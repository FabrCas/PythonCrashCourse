# le liste struttura data che può contenere diversi tipi (linguaggio non tipato)
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[4])
print(numbers[-1])  # accesso inverso possibile agli elementi di un array, -1 sarà sempre l'ultimo elemento della lista (snake logic)
print(numbers[-0])
print(numbers[-4])
# dynamic lists
numbers[0] = "uno"
# numbers["dieci"]= 9 >>> error (a differenza delle tables la chiave in una lista è sempre un intero)
# appending
numbers.append("sei")
# aggiungere ad un certo indice, facendo "shiftare" tutti gli elementi nella lista, non cancella nessun elemento
numbers.insert(7, 7)
print(numbers)
numbers.insert(0, 0)
print(numbers)
# cancellazione dati con il del statement
del numbers[0]
print(numbers)
# cancellazione elemento e ritorno valore, senza specificare .pop(), prende l'ultimo elemento (struttura dati pila)
elemento = numbers.pop()
print("elemento estratto " + str(elemento))
print(numbers)
print("\n")
# cancellazione e ritorno mirato
elemento = numbers.pop(3)
print("elemento estratto " + str(elemento))
print(numbers)
print("\n")

# rimozione di un elemento dato il valore, piuttosto che l'indice
numbers.remove(3)

print("rimuovo il numero 3 \n" + str(numbers) + "\n")

remove_element = "sei"
numbers.remove(remove_element)
print("rimuovo il numero 'sei' \n" + str(numbers) + "\n")

# ordinamento lista, in questa caso lista con elementi interi e stringhe è impossibile svolgere un ordinamento
numbers = ["zero", "uno", "due", "mille"]
numbers.sort()
print(str(numbers) + "\n")
# ordinamento decrescente
numbers.sort(reverse=True)
print(str(numbers) + "\n")
# possibilità di svolgere un'ordinamento temporaneo
numbers = [20, 4, 56, 1, 100, 0]
print("\n")
print(sorted(numbers))
print(numbers)
# attenzione all'ordinamento lessicografico, distinzione tre lower e upper case, codice ASCII associato
# capovolgere una lista
print("\n")
numbers.reverse()
print(numbers)
# utilizzo della funzione len() per conscere il valore della lunghezza di una lista
print("la lista e' lunga " + str(len(numbers)) + "\n")
