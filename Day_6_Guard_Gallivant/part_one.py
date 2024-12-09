grid = []

with open('input.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        grid.append(row)

xPos = 0
yPos = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '^':
            xPos = i
            yPos = j

count = 0
directions = ["up", "right", "down", "left"]
curDir = directions[0]

while 0 <= xPos < len(grid) and 0 <= yPos < len(grid[0]):
    if grid[xPos][yPos] == '#':
        if curDir == "up":
            xPos += 1
        elif curDir == "right":
            yPos -= 1
        elif curDir == "down":
            xPos -= 1
        elif curDir == "left":
            yPos += 1

        curDir = directions[(directions.index(curDir) + 1) % 4]
        continue

    if grid[xPos][yPos] != 'X':
        count += 1
        grid[xPos][yPos] = 'X'

    if curDir == "up":
        xPos -= 1
    elif curDir == "right":
        yPos += 1
    elif curDir == "down":
        xPos += 1
    elif curDir == "left":
        yPos -= 1

print(count)