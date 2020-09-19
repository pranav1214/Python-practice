import pandas as pd

data = pd.read_csv("student_score.csv")
print(data)

#shape --> returns a tuple(rows, columns)
print(data.shape)

#head() first 5 records head(n) first "n" records

print(data.head())

print(data.head(3))

#tail() last 5 records tail(n) last "n" records

print(data.tail())

print(data.tail(2))