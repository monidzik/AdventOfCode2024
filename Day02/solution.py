import numpy as np

def differences(arr):
   differences = np.abs(np.diff(arr))
   return np.all((differences >= 1) & (differences <= 3))

def make_it_safe(arr, sign):
    for i in range(len(arr)):
        removed = np.delete(arr, i)
        if sign == 0:
            if np.logical_and(np.all(np.diff(removed) > 0), differences(removed)):
                return True
        if sign == 1:
            if np.logical_and(np.all(np.diff(removed) < 0), differences(removed)):
                return True
    return False

with open('/Users/monikaidzik/code/AdventOfCode2024/Day02/input.txt', 'r') as f:
    data = [np.array(line.split(), dtype=int) for line in f]

# first part
i = 0
is_increasing = np.zeros(len(data))
is_decreasing = np.zeros(len(data))
diffs = np.zeros(len(data))
for arr in data:
    is_increasing[i] = np.logical_and(np.all(np.diff(arr) > 0), differences(arr))
    is_decreasing[i] = np.logical_and(np.all(np.diff(arr) < 0), differences(arr))
    diffs[i] = differences(arr)
    i = i+1
increasing_or_dicreasing = np.logical_or(is_increasing, is_decreasing)
sum_all = np.sum(increasing_or_dicreasing)
print(sum_all)

# second part
i = 0
is_increasing = np.zeros(len(data))
is_decreasing = np.zeros(len(data))
diffs = np.zeros(len(data))
for arr in data:
    is_increasing[i] = np.logical_or(np.logical_and(np.all(np.diff(arr) > 0), differences(arr)), make_it_safe(arr, 0))
    is_decreasing[i] = np.logical_or(np.logical_and(np.all(np.diff(arr) < 0), differences(arr)), make_it_safe(arr, 1))
    diffs[i] = differences(arr)
    i = i+1
increasing_or_dicreasing = np.logical_or(is_increasing, is_decreasing)
sum_all = np.sum(increasing_or_dicreasing)
print(sum_all)




