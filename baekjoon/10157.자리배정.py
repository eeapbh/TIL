import sys
sys.stdin = open('input.txt', 'r')

r, c = map(int, input().split())
k = int(input())
arr = [[0]*r for _ in range(c)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 1
arr[c-1][0] = cnt

x = c-1
y = 0
d = 0
while cnt < r*c:

    nx = x+dx[d]
    ny = y+dy[d]
    if 0<=nx<c and 0<=ny<r and arr[nx][ny] == 0:
        cnt += 1
        arr[nx][ny] = cnt
        x = nx
        y = ny
    else:
        d = (d + 1) % 4

# for t in arr:
#     print(*t)
x = y = 0
for i in range(c):
    for j in range(r):
        if arr[i][j] == k:
            x = j+1
            y = c-i
            break
if x == 0 or y == 0:
    print(0)
else:
    print(x, y)



