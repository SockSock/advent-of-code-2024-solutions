with open('input.txt', 'r') as file:
    disk_map = file.readline().strip()

flag = True
id_num = 0
formatted = []

for char in disk_map:
    if flag:
        for i in range(int(char)):
            formatted.append(id_num)
        id_num += 1
        flag = False
    else:
        for i in range(int(char)):
            formatted.append('.')
        flag = True

left = 0
right = len(formatted) - 1

while left < right:
    while left < len(formatted) and formatted[left] != '.':
        left += 1

    if left >= right:
        break

    formatted[left] = formatted[right]
    formatted[right] = '.'
    right -= 1

checksum = 0

for i, item in enumerate(formatted):
    if item == '.':
        break

    checksum += i * item

print(checksum)
