def read_file_to_2d_array(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def search_word_in_grid(grid, word):
    word_len = len(word)
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == word[i]):
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            if check_direction(r, c, 0, 1):
                count += 1
            if check_direction(r, c, 0, -1):
                count += 1

            if check_direction(r, c, 1, 0):
                count += 1
            if check_direction(r, c, -1, 0):
                count += 1

            if check_direction(r, c, 1, 1):
                count += 1
            if check_direction(r, c, -1, -1):
                count += 1
            if check_direction(r, c, 1, -1):
                count += 1
            if check_direction(r, c, -1, 1):
                count += 1

    return count

filename = "input.txt"
grid = read_file_to_2d_array(filename)
word = "XMAS"
count = search_word_in_grid(grid, word)

print(count)
