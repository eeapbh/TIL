#import sys
#sys.stdin = open("input.txt", "r")

t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    results = []
    for j in range(n-m+1):
        k = j
        s = 0
        for cnt in range(m):
            s = s + numbers[k]
            k = k+1
        results.append(s)

    print(f'#{i} {max(results) - min(results)}')
