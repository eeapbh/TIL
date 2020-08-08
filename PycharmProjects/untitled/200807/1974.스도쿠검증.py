import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
for tc in range(1, t+1):
    result = 1
    arr = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        test1 = set()
        test2 = set()
        for j in range(9):
            test1.add(arr[i][j])
            test2.add(arr[j][i])
        if len(test1) != 9:
            result = 0
            break
        if len(test2) != 9:
            result = 0
            break
    trg = 0
    for x in range(0,7, 3):
        for y in range(0, 7, 3):
            rec = set()
            for i in range(3):
                for j in range(3):
                    rec.add(arr[x+i][y+j])
            if len(rec) != 9:
                result = 0
                trg = 1
                break
        if trg:
            break
    print('#{} {}'.format(tc, result))

