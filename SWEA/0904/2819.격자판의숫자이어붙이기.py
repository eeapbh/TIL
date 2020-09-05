import sys
sys.stdin = open('input.txt', 'r')
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def check(x, y):
    global number
    if len(number) == 7:
        save.add(number)
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<4 and 0<=ny<4:
                number += arr[nx][ny]
                check(nx, ny)
                number = number[:len(number)-1]


t = int(input())

for tc in range(1, t+1):
    save = set()
    arr = [list(input().split()) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            number = arr[i][j]
            check(i, j)
    print('#{} {}'.format(tc, len(save)))