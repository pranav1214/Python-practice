import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("arrest_data.csv")

data['TOTAL_ARRESTS'] = data.sum(axis=1)
name = data["OFFICER_NAME"]
arrests = data['TOTAL_ARRESTS']
ex_value = [0,0,0.2]
col_value = ['green', 'blue', 'orange']

plt.pie(arrests, labels=name, radius =1.2, autopct= '%0.2f%%',colors=col_value, explode =ex_value, startangle=90, shadow=True)


plt.axis('equal')
plt.title("Arrests Made")

plt.show()
