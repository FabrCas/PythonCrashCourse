from matplotlib import pyplot as plt

x_values = list(range(1,1001)) # lista con numeri fino a 1000
y_values =  [x**2 for x in x_values]
print(y_values)

plt.scatter(x_values,y_values, s= 20) # per disegnare un funzione discontinua (punti)

# chart title and  label axes
plt.title("Square numbers", fontsize= 24)
plt.xlabel("Value", fontsize= 14)
plt.ylabel("Square of Value", fontsize= 14)

# set the range of each axis
plt.axis([0, 1100, 0, 1100000])

# size of tick labels
plt.tick_params(axis="both", which= "major", labelsize= 14)
plt.show()
