from sys import argv

with open(argv[1], 'r') as f:
    input_lines = f.read().splitlines()

print(sum([int(n[0]+n[-1]) for n in [''.join([c for c in line if str.isdigit(c)]) for line in input_lines]]))

