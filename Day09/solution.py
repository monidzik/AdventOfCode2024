import numpy as np

with open('/Users/monikaidzik/code/AdventOfCode2024/Day09/input_example.txt', 'r') as file:
    data = file.read()

data_array = np.array([int(d) for d in str(data)])

def unpack(data):
    unpacked_array = []
    j = 0
    idx = 0
    for i in range(data.shape[0]):
        for _ in range(data[i]):
            if j%2 == 0:
                unpacked_array.append(idx)
            else:
                unpacked_array.append(".")
        if j%2 == 0:
            idx += 1
        j+= 1
    return unpacked_array


def reorder_part1(data):
    looping = True
    i=0
    while looping:
        if "." not in data:
            looping = False
        if data[i]==".":
            for _ in range(9):
                if data[-1]==".":
                    data.pop()
                    if "." not in data:
                        looping=False
                else:
                    break
            if looping:
                data[i] = data.pop()
        i+=1
    return data


def how_many_numbers_to_remove(data, index):
    how_many_numbers_to_remove = 0
    what_number = data[index]
    for k in range(9):
        idx = index - k
        if data[idx]==what_number:
            how_many_numbers_to_remove+=1
        else:
            break
    return how_many_numbers_to_remove

def how_much_space_to_add(data, index):
    how_much_space_to_add = 0
    for k in range(9):
        idx = index + k
        if data[idx]==".":
            how_much_space_to_add+=1
        else:
            break
    return how_much_space_to_add


def reorder_part2(data):
    looping = True
    i=0
    j = len(data) - 1
    while looping:
        if j < 0:
            looping = False
        if data[j]==".":
            j -= 1
        else:
            to_remove = how_many_numbers_to_remove(data, j)
            for i in range(len(data)):
                if i <= j-to_remove:
                    if data[i] == ".":
                        to_add = how_much_space_to_add(data, i)
                        if to_remove <= to_add:
                            for k in range(to_remove):
                                data[i+k]=data[j-k]
                                data[j-k] = "."
                            j = j-to_remove
                            break
                else:
                    j = j-to_remove
                    break
    return data


def count_sum(data):
    checksum = 0
    for i in range(len(data)):
        checksum += i*data[i]
    return checksum


def count_sum2(data):
    checksum = 0
    for i in range(len(data)):
        if data[i] == ".":
            data[i] = int(0)
    data=np.array(data, int)
    for i in range(len(data)):
        checksum += i*data[i]
    return checksum


unpacked_array = unpack(data_array)
unpacked_array2 = np.copy(unpacked_array)
reorderred_array = reorder_part1(unpacked_array)
print("part1: ", count_sum(reorderred_array))
reorderred_array2 = reorder_part2(unpacked_array2)
print("part2: ", count_sum2(reorderred_array2))
