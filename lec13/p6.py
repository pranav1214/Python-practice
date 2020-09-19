import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("student_score.csv")
name = data["NAME"].tolist()
sem1 = data["SEM1"].tolist()


plt.plot(name, sem1, linewidth=5, color='green', marker='p', markersize=10, markerfacecolor='r')
plt.xlabel("Names")
plt.ylabel("SEM1")
plt.title("Sem1 Performance")
plt.grid()
plt.savefig("sem1.png")
plt.savefig("sem1.pdf")
plt.show()