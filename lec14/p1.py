import pandas as pd
import matplotlib.pyplot as plt

months = ['June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mumbai = [82.5, 83.06,83.61,85.6,90.75,85.24,84.06]

plt.plot(months, mumbai, linewidth =2, marker='o',markerfacecolor='b', label='Mumbai')

plt.xlabel("Months")
plt.ylabel("Prices")
plt.title("Petrol Prices")
plt.grid()
plt.legend(shadow=True)
plt.show()
