left_nums = []
right_nums = []

with open('input.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_nums.append(left)
        right_nums.append(right)

sim_score = 0
count = {}

for num in right_nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for i in range(len(left_nums)):
    first = left_nums[i]
    second = 0
    if first in count:
        second = count[first]

    sim_score += first * second

print(sim_score)
