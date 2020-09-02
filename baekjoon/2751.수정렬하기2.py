import sys
N = int(sys.stdin.readline())
numbers = [0]*10000
for _ in range(N):
    numbers[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    [print(i + 1) for _ in range(numbers[i])]
