import sys
sys.stdin = open('input.txt','r')

# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)
def action(d):
    global sx
    global sy
    if d == 'U':
        arr[sx][sy] = '^'
        if sx-1 >= 0:
            if arr[sx-1][sy] == '.':
                arr[sx][sy] = '.'
                arr[sx-1][sy] = '^'
                sx = sx-1
    elif d == 'D':
        arr[sx][sy] = 'v'
        if sx+1 < h:
            if arr[sx+1][sy] == '.':
                arr[sx][sy] = '.'
                arr[sx+1][sy] = 'v'
                sx = sx+1
    elif d == 'L':
        arr[sx][sy] = '<'
        if sy-1 >= 0:
            if arr[sx][sy-1] == '.':
                arr[sx][sy] = '.'
                arr[sx][sy-1] = '<'
                sy = sy-1
    elif d == 'R':
        arr[sx][sy] = '>'
        if sy+1<w:
            if arr[sx][sy+1] == '.':
                arr[sx][sy] = '.'
                arr[sx][sy+1] = '>'
                sy = sy+1

    elif d == 'S':
        if arr[sx][sy] == '^':
            nx = sx
            while 1:
                nx = nx-1
                if 0<=nx<h:
                    if arr[nx][sy] == '*':
                        arr[nx][sy] = '.'
                        break
                    if arr[nx][sy] == '#':
                        break
                else:
                    break
        elif arr[sx][sy] == 'v':
            nx = sx
            while 1:
                nx = nx+1
                if 0<=nx<h:
                    if arr[nx][sy] == '*':
                        arr[nx][sy] = '.'
                        break
                    if arr[nx][sy] == '#':
                        break
                else:
                    break

        elif arr[sx][sy] == '<':
            ny = sy
            while 1:
                ny = ny-1
                if 0<=ny<w:
                    if arr[sx][ny] == '*':
                        arr[sx][ny] = '.'
                        break
                    if arr[sx][ny] == '#':
                        break
                else:
                    break

        elif arr[sx][sy] == '>':
            ny = sy
            while 1:
                ny = ny+1
                if 0<=ny<w:
                    if arr[sx][ny] == '*':
                        arr[sx][ny] = '.'
                        break
                    if arr[sx][ny] == '#':
                        break
                else:
                    break

t = int(input())
for tc in range(1, t+1):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    n = int(input())
    info = input()
    for i in range(h):
        for j in range(w):
            if arr[i][j] in '<>^v':
                sx, sy = i, j
                break

    for d in info:
        action(d)
    print('#{}'.format(tc), end=' ')
    for a in arr:
        for b in a:
            print(b, end='')
        print()

