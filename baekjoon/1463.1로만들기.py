import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

n = int(input())
arr = deque([[n, 0]])

while 1:
    x, c = arr.popleft()

    if x == 1:
        break
    if x % 3 == 0:
        arr.append([x/3, c+1])
    if x % 2 == 0:
        arr.append([x/2, c+1])
    arr.append([x-1, c+1])

print(c)
