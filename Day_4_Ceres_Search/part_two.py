def read_file_to_2d_array(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]


def search_cross_mas_in_grid(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(0, rows - 2):
        for c in range(0, cols - 2):
            cross_chars = [
                grid[r][c],
                grid[r][c + 2],
                grid[r + 1][c + 1],
                grid[r + 2][c],
                grid[r + 2][c + 2]
            ]

            cross_string = ''.join(cross_chars)
            print(cross_string)

            if cross_string == "MSAMS" or cross_string == "SSAMM" or cross_string == "MMASS" or cross_string == "SMASM":
                count += 1

    return count

filename = "input.txt"
grid = read_file_to_2d_array(filename)
count = search_cross_mas_in_grid(grid)

print(count)
