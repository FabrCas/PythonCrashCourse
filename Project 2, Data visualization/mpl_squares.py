import matplotlib.pyplot as plt

def square(x):
    return x**2

numbers_input= list(range(51))
squares= []
for number in numbers_input:
    squares.append(square(number))

plt.plot(numbers_input, squares, linewidth= 5) #linewidth larghezza tratto

# impostare etichette al grafico
plt.title("Quadrati dei numeri fino a 50", fontsize= 24)
plt.xlabel("x", fontsize = 14 )
plt.ylabel("y = x^2", fontsize= 14)
# impostazione valori sugli assi
plt.tick_params(axis="both", labelsize= 14)
plt.show()

