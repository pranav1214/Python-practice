import matplotlib.pyplot as plt

expenses = ['Food', 'Bills', 'Travel', 'Others']

usages =[500, 2000, 680, 1500]
ex_value = [0,0.1,0,0]
co_value = ['lightblue', 'maroon', 'orange', 'purple']

plt.pie(usages, labels=expenses, radius=1.2, autopct='%0.2f%%', explode = ex_value, shadow=True, startangle=15, colors= co_value)

plt.axis('equal')
plt.title("Monthly Expenses")
plt.savefig("me.pdf")
plt.show()