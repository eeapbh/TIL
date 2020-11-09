import sys
sys.stdin = open('input.txt', 'r')

line = input()
arr = []
for i in range(len(line)):
    tmp = line[i:]
    arr.append(tmp)
arr.sort()
for a in arr:
    print(a)