import sys
sys.stdin = open('input.txt', 'r')

def inOrder(v):
    if len(arr[v]) >=1:
        inOrder(arr[v][0])
    result.append(v)
    if len(arr[v]) == 2:
        inOrder(arr[v][1])

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    arr = [[] for _ in range(n+1)]
    i = 1
    while 1:
        arr[i].append(2*i)
        if 2*i == n:
            break
        arr[i].append((2*i) + 1)
        if (2*i)+1 == n:
            break
        i += 1

    result = [0]

    inOrder(1)
    print('#{} {} {}'.format(tc, result.index(1), result.index(n//2)))





