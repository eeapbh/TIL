import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]


    result = 1
    for i in range(9):
        set1 = set()
        set2 = set()
        for j in range(9):
            set1.add(arr[i][j])
            set2.add(arr[j][i])
        if len(set1) != 9:
            result = 0
            break

        if len(set2) != 9:
            result = 0
            break
    trg = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            set3 = set()
            for x in range(3):
                for y in range(3):
                    set3.add(arr[i+x][j+y])
            if len(set3) != 9:
                result = 0
                trg = 1
                break
        if trg:
            break

    print(f'#{tc} {result}')

