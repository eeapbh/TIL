import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dh = [-1, 0, 1]

def check(save):
    for i in range(len(save)):
        x, y, h = save[i][1], save[i][2], save[i][0]
        for t in range(3):
            nh = h+dh[t]
            if 0<=nh<h and arr[nh][x][y] == 0:
                arr[nh][x][y] = 1
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<n and 0<=ny<m and arr[h][nx][ny] == 0:
                arr[h][nx][ny] = 1
    c = sum(sum(arr, []), [])
    return c.count(0)

m, n, h = map(int, input().split())
arr = []
for i in range(h):
    tmp =[list(map(int, input().split())) for _ in range(n)]
    arr.append(tmp)
# print(arr)
# print(len(arr))

c = sum(sum(arr, []), [])
cnt = 0
wcnt = 0
t = c.count(0)
while wcnt<m*n:
    if t == 0:
        break
    wcnt += 1
    save = []
    for a in range(h):
        for i in range(n):
            for j in range(m):
                if arr[a][i][j] == 1:
                    save.append((a, i, j))
    s = check(save)
    cnt += 1
    if s== 0:
        break
    if t != s:
        t = s
    else:
        cnt = -1
        break
print(cnt)
