

import math
m = int(input())
n = int(input())

def prime(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    else:
        cnt = 0
        for i in range(1, int(math.sqrt(x))+1):
            if x % i == 0:
                cnt += 2

        if cnt == 2:
            return 1

        else:
            return 0

arr = []
for i in range(m, n+1):
    if prime(i) == 1:
        arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
