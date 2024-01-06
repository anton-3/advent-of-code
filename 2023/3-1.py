from sys import argv

with open(argv[1], 'r') as f:
    input_lines = f.read().splitlines()

LINE_LENGTH = len(input_lines)
NUM_LINES = len(input_lines[0])

def check_adjacent(i, j):
    adj_coords = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    # filter out overflow and underflow
    adj_coords = [coord for coord in adj_coords if -1 not in coord and LINE_LENGTH not in coord and NUM_LINES not in coord]
    adj = [input_lines[coord[0]][coord[1]] for coord in adj_coords]
    symbols = [c for c in adj if c != '.' and not c.isdigit()]
    return len(symbols) > 0

def get_number_at(i, j):
    if not input_lines[i][j].isdigit():
        return
    l = r = j
    while l > 0 and input_lines[i][l-1].isdigit():
        l -= 1
    while r < LINE_LENGTH - 1 and input_lines[i][r+1].isdigit():
        r += 1
    return int(input_lines[i][l:r+1])

# numbers that are adjacent to a symbol
part_numbers = []

for i, line in enumerate(input_lines):
    j = 0
    while j < len(line):
        if line[j].isdigit() and check_adjacent(i, j):
            part_numbers.append(get_number_at(i, j))
            j += 1
            # advance to end of number
            while j < len(line) and line[j].isdigit():
                j += 1
        else:
            j += 1

print(sum(part_numbers))
