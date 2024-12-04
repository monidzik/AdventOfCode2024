import numpy as np

with open('/Users/monikaidzik/code/AdventOfCode2024/Day04/input.txt', 'r') as file:
    data = file.read().splitlines()     

def rotate_90_degrees(data):
    array = np.array([list(line) for line in data])
    rotated = np.rot90(array)
    string_list = [''.join(row) for row in rotated]
    return string_list


def move_letters(row):
    non_o = [char for char in row if char != 'O']
    return (non_o + ['O'] * (len(row) - len(non_o)))


def rotate_45_degrees(data):
    array = np.array([list(line) for line in data])
    n = array.shape[0]
    new_size = 2 * n - 1  
    output_shape = (new_size, n)
    rotated = np.full(output_shape, 'O', dtype=array.dtype)
    middle=n-1
    for i in range(n): 
        for j in range(n): 
            m = middle+i-j
            rotated[m][i] = array[i][j]
    result = np.array([move_letters(row) for row in rotated])

    string_list = [''.join(row) for row in rotated]
    return string_list


def count_occurances(data, word):
    matches = [s.count(word) for s in data]
    return sum(matches)

count = 0
count = count_occurances(data, "XMAS")
rotated_90 = rotate_90_degrees(data)
rotated_45 = rotate_45_degrees(data)

count += count_occurances(rotated_45, "XMAS")
count += count_occurances(rotated_90, "XMAS")

rotated_135 = rotate_45_degrees(rotated_90)
rotated_180 = rotate_90_degrees(rotated_90)
count += count_occurances(rotated_135, "XMAS")
count += count_occurances(rotated_180, "XMAS")

rotated_225 = rotate_45_degrees(rotated_180)
rotated_270 = rotate_90_degrees(rotated_180)
count += count_occurances(rotated_225, "XMAS")
count += count_occurances(rotated_270, "XMAS")

rotated_315 = rotate_45_degrees(rotated_270)
count += count_occurances(rotated_315, "XMAS")

print(count)

def count_kernel_matches(input_array, kernel):
    count = 0
    array = np.array([list(line) for line in input_array])
    rows, cols = array.shape

    for i in range(rows - 2):
        for j in range(cols - 2):
            subarray = array[i:i+3, j:j+3]
            match = True
            for ki in range(3):
                for kj in range(3):
                    if kernel[ki, kj] is not None and kernel[ki, kj] != subarray[ki, kj]:
                        match = False
                        break
                if not match:
                    break
            if match:
                count += 1
    return count
count = 0

kernel = np.array([
    ['M', None, 'M'],
    [None, 'A', None],
    ['S', None, 'S']
])

array = np.array([list(line) for line in data])
count += count_kernel_matches(array, kernel)
rotated_90 = rotate_90_degrees(data)
count += count_kernel_matches(rotated_90, kernel)
rotated_180 = rotate_90_degrees(rotated_90)
count += count_kernel_matches(rotated_180, kernel)
rotated_270 = rotate_90_degrees(rotated_180)
count += count_kernel_matches(rotated_270, kernel)
print(count)