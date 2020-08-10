import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
def turn(li):
    r = []
    rs = []
    n = len(li)
    for i in range(n):
        for j in range(n):
            r.append(li[j][i])
        r.reverse()
        rs.append(r)
        r = []
    return rs
for tc in range(1, t+1):
    save90 = []
    save180 = []
    save270 = []
    save = []
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    save90 = turn(arr)
    save180 = turn(save90)
    save270 = turn(save180)


    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(save90[i][j], end='')
        print(' ', end = '')
        for j in range(n):
            print(f'{save180[i][j]}', end='')
        print(' ', end='')
        for j in range(n):
            print(f'{save270[i][j]}', end='')
        print()

