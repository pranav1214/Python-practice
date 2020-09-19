import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("jobs.csv")
lang = data["LANGUAGE"].tolist()
job17 = data["JOBS_2017"].tolist()
job18 = data["JOBS_2018"].tolist()

x = np.arange(len(lang))
plt.bar(x, job17, label='2017', width=0.25)
plt.bar(x+0.25, job18, label='2018', width=0.25)
plt.xticks(x,lang)


plt.xlabel("Languages")
plt.ylabel("Jobs")
plt.title("Jobs Availability")
plt.grid()
plt.legend(shadow=True)
plt.show()