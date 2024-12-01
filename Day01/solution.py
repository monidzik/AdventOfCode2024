import numpy as np

data = np.loadtxt('C:/Users/monik/PycharmProjects/AdventOfCode2024/Day01/input.txt', dtype=int)

column_1 = np.sort(data[:, 0])
column_2 = np.sort(data[:, 1])
difference_table = np.sum(abs(column_1 - column_2))

print(difference_table) # 1889772

occurrences = np.array([(column_2 == i).sum() for i in column_1])
score = occurrences*column_1

sum_score = np.sum(score) 
print(sum_score) # 23228917
