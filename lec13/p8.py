import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("petrol_prices.csv")
print(data)

month = data["MONTH"].tolist()
mumbai = data["MUMBAI"].tolist()
delhi = data["DELHI"].tolist()
chennai = data["CHENNAI"].tolist()

plt.plot(month, mumbai, linewidth=2, marker='o', markersize=10, markerfacecolor='b', label='Mumbai')

plt.plot(month, delhi, linewidth=2, marker='o', markersize=10, markerfacecolor='y', label='Delhi')

plt.plot(month, chennai, linewidth=2, marker='o', markersize=10, markerfacecolor='g', label='Chennai')




plt.xlabel("Months")
plt.ylabel("Prices")
plt.title("Petrol Prices")
plt.grid()
plt.legend(shadow=True)
plt.show()