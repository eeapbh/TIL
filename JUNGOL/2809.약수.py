import math

n = int(input())
sq = (int(math.sqrt(n)))
arr = [0]*10000
for i in range(1, sq+1):
    if n % i == 0:
        arr.append(i)
        if n // i != i:
            arr.append(n//i)
arr.sort()
for i in arr:
    if i > 0:
        print(i, end=' ')
