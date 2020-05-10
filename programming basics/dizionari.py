# dizionari, coppie chiave valore, simili alle mappe in Java senza la limitazione del tipo per chaive e valore
alien_0 = {'color': 'green', 'points': 5}  # definizione

print(alien_0['color'])  # accesso

# aggiungere una nuova coppia chiave-valore
alien_0['x_position'] = 0
alien_0['y_position'] = 25

alien_0[34] = 34
# gia presente una coppia con la chiave 'color', quindi sovrascrittura
alien_0['color'] = 'yellow'
print(alien_0)

# semplice esempio di utilizzo di un dizionario
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

if alien_0['speed'] == 'slow':
    incremento = 1
elif alien_0['speed'] == 'medium':
    incremento = 2
elif alien_0['speed'] == 'fast':
    incremento = 3

alien_0['x_position'] += incremento
print(alien_0['x_position'])

# rimozione di una coppia chiave-valore con del statement
del alien_0['speed']
print(alien_0)

# iterare in un dizionario
# il metodo items() ritorna una lista di elementi chiave-valore
for key, value in alien_0.items():
    print("key: " + str(key))
    print("value: " + str(value))

print("*******************************")
# per iterare tra le chiavi
for key in alien_0.keys():
    print("key: " + str(key))

if 'attempt' not in alien_0.keys():
    print("attemp non e' una chiave")

# ad esempio potremmo voler volere le chiavi ordinate

for key in sorted(alien_0.keys()):
    print("key: " + str(key))


# iterazioni tra tutti i valori di un dizionario

for value in alien_0.values():
    print("value: " + str(value))

# quando iteriamo sui valori non viene fatto alcun controllo per cio' che riguarda la ripetitivita'
# per fare cio' possiamo utilizzare la funzione set() che "eliminia i doppioni"

print("****************************************")
alien_0['force'] = 25

for value in alien_0.values():
    print("value: " + str(value))

print("****************************************")

for value in set(alien_0.values()):
    print("value: " + str(value))

# strutture innestate
# mettere dizionari in una lista
print("\n***************strutture innestate*************************\n")
diz1 = {'color': 'blue', 'number': 34}
diz2 = {'color': 'green', 'number': 100}
diz3 = {'color': 'red', 'number': 45}

lista = [diz1, diz2, diz3]

print(lista)


print(list(range(0, 30)))

# mettere liste in un dizionario

pizza = {
    'tipologia': 'margherita',
    'ingredienti': ['mozzarella', 'pomodoro', 'prezzemolo']
}

print(pizza)

# dizionario in un dizionario

print("\n***************dizionario in dizionario******************\n")
users = {
    'einstein': {
        'last': 'einstein',
        'first': 'albert',
        'location': 'princeton'
    },
    'mcurie': {
        'last': 'curie',
        'first': 'marie',
        'location': 'paris'
    }
}

for username, user in users.items():
    print("\n")
    print("Username: " + str(username))
    for key, value in user.items():
        print(str(key) + ": " + str(value))
