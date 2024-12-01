from sys import argv

filename = argv[1]
with open(filename, 'r') as f:
    lines = f.read().splitlines()

list1 = []
list2 = []
for line in lines:
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

result = 0
for i in range(len(list1)):
    result += abs(list1[i] - list2[i])

print(result)
