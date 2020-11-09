import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(e)]
     
    arr = sorted(arr, key=lambda x:x[2])
    p = list(range(v+1))


    ans = 0
    cnt = 0
    idx = 0

    while cnt < v:
        x = arr[idx][0]
        y = arr[idx][1]

        if find_set(x) != find_set(y):# 같은 그룹이 아닐때
            union(x, y)
            cnt += 1
            ans += arr[idx][2]
        idx += 1

    print('#{} {}'.format(tc, ans))