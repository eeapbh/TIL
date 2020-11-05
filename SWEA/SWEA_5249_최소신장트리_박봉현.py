import sys
sys.stdin = open('input.txt', 'r')

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])

    return p[x]


def union(x, y):
    p[find_set(x)] = find_set(y)


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[]*(v+1) for _ in range(v+1)]

    edges = [list(map(int, input().split())) for _ in range(e)]
    edges = sorted(edges, key=lambda x:x[2])
    p = [-1]*(v+1)
    for i in range(v+1):
        make_set(i)

    ans = 0
    cnt = 0
    idx = 0
    while cnt < v:
        if find_set(edges[idx][0]) != find_set(edges[idx][1]):
            union(edges[idx][0], edges[idx][1])
            cnt += 1
            ans += edges[idx][2]
        idx += 1
    print('#{} {}'.format(tc, ans))