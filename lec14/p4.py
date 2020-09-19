import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("medals.csv")
country = data["COUNTRY"].tolist()
medals = data["GOLD_MEDAL"].tolist()
ex_value = [0.2, 0,0,0]

plt.pie(medals, labels=country, radius=1.2, autopct='%0.2f%%', explode = ex_value,shadow=True)

plt.axis('equal')
plt.title("Olympics Performance")

plt.show()