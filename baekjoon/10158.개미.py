import sys
sys.stdin = open('input.txt', 'r')

r, c = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
arr = [[0]*(r+1) for _ in range(c+1)]
dx = [-1, -1, 1, -1]
dy = [1, -1, -1, -1]
cnt = 0
d = 0
while cnt <= t+1:
    nx = p+dx[d]
    ny = q+dy[d]
    if 0<=nx<c+1 and 0<=ny<r+1:
        p = nx
        q = ny
    else:
        d = (d+1)%4
    cnt += 1

print(p, q)
