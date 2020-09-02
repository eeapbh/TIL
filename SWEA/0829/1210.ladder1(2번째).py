import sys
sys.stdin = open('input.txt', 'r')
dr = [0, 0, -1]
dc = [-1, 1, 0]
def DFS(x, y):
    global result
    visited.append((x, y))
    if x == 0:
        result = y
        return

    for i in range(3):
        nx = x+dr[i]
        ny = y+dc[i]
        if 0<=nx<100 and 0<=ny<100:
            if not (nx, ny) in visited and arr[nx][ny] == 1:
                return DFS(nx, ny)

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    start_y = arr[99].index(2)

    result = 0
    visited = []
    DFS(99, start_y)

    print('#{} {}'.format(tc, result))
