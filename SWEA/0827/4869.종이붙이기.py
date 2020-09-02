def check(n):

    if n > 2 and len(arr)<=n:
        arr.append(2*check(n-2) + check(n-1))
    return arr[n]

t = int(input())

for tc in range(1, t+1):
    arr = [0, 1, 3]
    N = int(input())
    n = N//10

    print('#{} {}'.format(tc, check(n)))




