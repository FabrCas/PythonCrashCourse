# semplice uso dell'if-else statements
num = [1, 2, 3]

for n in num:
    if n == 1:
        print("numero uno")
    else:
        print("numero due o tre")

a = 10
if a != 40:
    print("a non e' 40")
if a >= 5:
    print("a maggiore di 5")

# condizioni multiple

if a == 10 and 10 != 100:  # analogo con or
    a = 100

# verifica elemento in una lista

if 1 in num:
    print(num)

# catena if-elif-else

for n in num:  # evita il classico uso di un for per scorrere una lista e controllare tutti gl elementi
    if n == 1:
        print("numero uno")
    elif n == 2:
        print("numero due")
    else:
        print("numero tre")

emptyList = []

# verificare se una lista è vuota
if emptyList:
    print("lista con elementi")
else:
    print("lista vuota")
