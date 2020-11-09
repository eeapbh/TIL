import sys
sys.stdin = open('input.txt', 'r')

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]
def union(x, y):
    p[find_set(y)] = p[find_set(x)]


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    p = [0]*(n+1)
    for i in range(n+1):
        make_set(i)

    info = list(map(int, input().split()))
    for i in range(m):
        x = info[2*i]
        y = info[2*i+1]
        union(x, y)
    for i in range(1, n+1):
        find_set(i)
    print(p)
    print(len(set(p))-1)



