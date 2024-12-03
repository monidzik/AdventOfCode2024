import re

with open('/Users/monikaidzik/code/AdventOfCode2024/Day03/input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

with open('/Users/monikaidzik/code/AdventOfCode2024/Day03/input_example2.txt', 'r', encoding='utf-8') as file:
    input_example = file.read()
#print(input_example)

pattern =  r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))"
matches = re.findall(pattern, content);

result = [0, 0]
enabled = 1

for match in matches:
    if match[0]:
        enabled = 1
    elif match[1]:
        enabled = 0
    else:
        product = int(match[3]) * int(match[4])
        result[0] += product
        result[1] += product * enabled

print(result)