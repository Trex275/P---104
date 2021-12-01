import csv
from collections import Counter

with open("C104/archive/SOCR-HeightWeight.csv")as file: 
    reader = csv.reader(file)
    data = list(reader)

data.pop(0)
height = []
for i in range(len(data)): 
    newdata = data[i][1]
    height.append(newdata)
g = len(height)
sum = 0
for h in height: 
    sum = sum + float (h)
mean = sum/g
print(mean)


height.sort()
if g%2 == 0:
    median = float(height[g//2])
    median2 = float(height[g//2 -1])
    median = (median + median2)/2
    print(median)
else: 
    median = float(height[g//2])
    print(median)

