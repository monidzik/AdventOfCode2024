import numpy as np

with open('/Users/monikaidzik/code/AdventOfCode2024/Day07/input.txt', 'r') as f:
    data = f.read().splitlines()

results = []
numbers_all = []
for line in data:
    number, numbers = line.split(": ")
    result = int(number)
    numbers_line = list(map(int, numbers.split()))
    results.append(result)
    numbers_all.append(numbers_line)

is_result = 0
counter = 0
for line in numbers_all:
    list1 = []
    for i in range(len(line) - 1):
        if i==0:
            list1.append(line[i] + line[i+1])
            list1.append(line[i] * line[i+1])
            new_number = int(str(line[i])+str(line[i+1]))
            list1.append(new_number)
            new_list = []
        else:
            for items in list1:
                new_list.append(items + line[i+1])
                new_list.append(items * line[i+1])
                new_number = int(str(items)+str(line[i+1]))
                new_list.append(new_number)
            list1 = new_list.copy()
            new_list = []
    if results[counter] in list1:
        is_result += results[counter]
    counter += 1
print(is_result)