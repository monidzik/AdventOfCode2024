import numpy as np

with open('/Users/monikaidzik/code/AdventOfCode2024/Day05/input.txt', 'r') as f:
    data = f.read().splitlines()  

def is_there_rule(line, i, j):
    if str(line[i]) + "|" + str(line[j]) in rules:
        return True
    else:
        return False

def get_middle(line):
    length = len(line)
    return line[int(length/2)]

rules = set()
numbers = []
one_line = []
i = 0
for line in data:
    if "|" in line:
        rules.add(line)
    else:
        if len(line)>0:
            numbers.append(list(map(int, line.split(','))))

sum_middle = 0
sum_middle_2 = 0
for line in numbers:
    is_ok = True
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if not is_there_rule(line, i, j):
                is_ok = False
    if is_ok:
        sum_middle += get_middle(line)
    else:
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if not is_there_rule(line, i, j):
                    line[i], line[j] = line[j], line[i]
        sum_middle_2 += get_middle(line)
        
print(sum_middle)
print(sum_middle_2)
