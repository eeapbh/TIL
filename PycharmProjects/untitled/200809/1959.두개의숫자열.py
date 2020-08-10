import sys
sys.stdin = open('input.txt', 'r')
t = int(input())

for tc in range(1, t+1):
    n, m  = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    results = []
    result = 0
    if n< m :
        for i in range(m-n+1):
            for j in range(n):
                result += arr2[i+j]*arr1[j]

            results.append(result)
            result = 0
    else:
        for i in range(n-m+1):
            for j in range(m):
                result += arr1[i+j]*arr2[j]
            results.append(result)
            result = 0
    print(f'#{tc} {max(results)}')
