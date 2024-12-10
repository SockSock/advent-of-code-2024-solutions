left_nums = []
right_nums = []

with open('input.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_nums.append(left)
        right_nums.append(right)

left_nums.sort()
right_nums.sort()

total_dist = 0

for i in range(len(left_nums)):
    total_dist += abs(left_nums[i] - right_nums[i])

print(total_dist)
