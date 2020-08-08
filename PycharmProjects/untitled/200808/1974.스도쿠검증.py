import sys
sys.stdin = open('input.txt', 'r')
t = int(input())

for tc in range(1, t+1):
    result = 1
    arr = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        garo = set()
        sero = set()
        for j in range(9):
            garo.add(arr[i][j])
            sero.add(arr[j][i])
        if len(garo) != 9:
            result = 0
            break
        if len(sero) != 9:
            result = 0
            break

    count = 0

    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            box = set()
            for a in range(3):
                for b in range(3):
                    box.add(arr[x+a][y+b])
            if len(box) != 9:
                count = 1
                result = 0
                break
        if count:
            break
    print(f'#{tc} {result}')