from sys import argv

with open(argv[1], 'r') as f:
    input_lines = f.read().splitlines()

LINE_LENGTH = len(input_lines)
NUM_LINES = len(input_lines[0])

def get_adjacent(i, j):
    adj_coords = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    # filter out overflow and underflow
    return [coord for coord in adj_coords if -1 not in coord and LINE_LENGTH not in coord and NUM_LINES not in coord]

def get_number_at(i, j):
    if not input_lines[i][j].isdigit():
        return
    l = r = j
    while l > 0 and input_lines[i][l-1].isdigit():
        l -= 1
    while r < LINE_LENGTH - 1 and input_lines[i][r+1].isdigit():
        r += 1
    return int(input_lines[i][l:r+1])

part_numbers = []

for i, line in enumerate(input_lines):
    for j, c in enumerate(line):
        if c != '*':
            continue
        adj_coords = get_adjacent(i, j)
        digit_coords = [coord for coord in adj_coords if input_lines[coord[0]][coord[1]].isdigit()]
        parts = set()
        for coord in digit_coords:
            parts.add(get_number_at(coord[0], coord[1]))
        if len(parts) != 2:
            continue
        p = list(parts)
        part_numbers.append(p[0] * p[1])

print(sum(part_numbers))
