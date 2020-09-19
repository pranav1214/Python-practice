import pandas as pd

data = pd.read_csv("student_score.csv")
print(data)

# slicing is used for data from any position to any position
# [start:stop]		[start:stop:stepsize]

print(data[:])
print(data[3:])
print(data[:2])
print(data[2:5])
print(data[-2:])
print(data[5:2])
print(data[5:2:-1])
print(data[2:20:2])