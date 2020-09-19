import numpy as np
import matplotlib.pyplot as plt

products = ['Laptop', 'Printer', 'Router']
reena = [10, 25, 15]
veena = [5, 30, 12]

x = np.arange(len(products))
plt.bar(x, reena, width=0.25, label='Reena')
plt.bar(x+0.25, veena, width=0.25, label='Veena')
plt.xticks(x, products)

plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Perfomance Analysis")
plt.grid()
plt.legend(shadow=True)
plt.show()