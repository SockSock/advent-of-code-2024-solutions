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


def is_safe_after_removal(lst):
    if (is_decreasing(lst) or is_increasing(lst)) and valid_two_adjacent_levels(lst):
        return True

    for i in range(len(lst)):
        modified_list = lst[:i] + lst[i + 1:]
        if (is_decreasing(modified_list) or is_increasing(modified_list)) and valid_two_adjacent_levels(modified_list):
            return True

    return False


safe_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        numbers_as_strings = line.strip().split()
        numbers_list = [int(num) for num in numbers_as_strings]

        if is_safe_after_removal(numbers_list):
            safe_count += 1

print(safe_count)
