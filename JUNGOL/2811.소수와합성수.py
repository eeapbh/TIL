import sys
sys.stdin = open('input.txt')

import math
info = list(map(int, input().split()))
def prime(x):
    if x == 1:
        return 'number one'
    if x == 2:
        return 'prime number'
    else:
        cnt = 0
        for i in range(1, int(math.sqrt(x))+1):
            if x % i == 0:
                cnt += 2

        if cnt == 2:
            return 'prime number'

        else:
            return 'composite number'

for i in info:
    print(prime(i))