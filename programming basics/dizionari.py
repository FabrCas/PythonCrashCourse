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

#iterare in un dizionario
