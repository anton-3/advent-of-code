from sys import argv
from collections import defaultdict

filename = argv[1]
with open(filename, 'r') as f:
    lines = f.read().splitlines()

list1 = []
list2 = []
for line in lines:
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))

counts = defaultdict(int)
for num in list2:
    counts[num] += 1

result = 0
for num in list1:
    result += num * list2.count(num)
print(result)
