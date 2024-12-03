import re

pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
total = 0

with open('input.txt', 'r') as file:
    for line in file:
        matches = re.findall(pattern, line)

        for match in matches:
            x, y = map(int, match)
            total += x * y

print(total)
