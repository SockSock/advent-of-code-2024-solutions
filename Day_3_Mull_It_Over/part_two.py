import re

total = 0
mul_enabled = True

pattern = re.compile(r"(do\(\))|(don't\(\))|mul\((\d*),\s*(\d*)\)")

with open('input.txt', 'r') as file:
    for line in file:
        matches = pattern.findall(line)

        for match in matches:
            if match[0] == "do()":
                mul_enabled = True
            elif match[1] == "don't()":
                mul_enabled = False
            elif match[2] and match[3]:
                if mul_enabled:
                    x, y = map(int, (match[2], match[3]))
                    total += x * y

print(f"Final total: {total}")
