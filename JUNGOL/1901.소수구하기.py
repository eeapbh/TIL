import math

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

n = int(input())
for i in range(n):
    m = int(input())
    ans = []
    for j in range(1000000):
        if prime(m-j) == 1:
            ans.append(m-j)
        if prime(m+j) == 1 and m-j != m+j:
            ans.append(m+j)
        if len(ans) > 0:
            break

    for i in ans:
        print(i, end=' ')
    print()

