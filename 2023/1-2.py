from sys import argv

with open(argv[1], 'r') as f:
    input_lines = f.read().splitlines()

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def fix(s):
    for i, num in enumerate(nums):
        s = s.replace(num, num + str(i+1) + num)
    return s

print(sum([int(n[0]+n[-1]) for n in [''.join([c for c in fix(line) if str.isdigit(c)]) for line in input_lines]]))
