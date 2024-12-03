def is_increasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True

def is_decreasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            return False
    return True

def valid_two_adjacent_levels(lst):
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1] or abs(lst[i + 1] - lst[i]) > 3:
            return False
    return True

safe_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        numbers_as_strings = line.strip().split()
        numbers_list = [int(num) for num in numbers_as_strings]

        if (is_decreasing(numbers_list) or is_increasing(numbers_list)) and valid_two_adjacent_levels(numbers_list):
            safe_count += 1

print(safe_count)
