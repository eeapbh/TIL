t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        check_r = set()
        check_c = set()
        for j in range(9):
            check_r.add(arr[i][j])
            check_c.add(arr[j][i])
        if len(check_c) != 9:
            result = 0
            break
        if len(check_r) != 9:
            result = 0
            break
    trg = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = set()
            for a in range(3):
                for b in range(3):
                    check.add(arr[i+a][i+b])

            if len(check) != 9:
                result = 0
                trg = 1
                break

        if trg:
            break
    print('#{} {}'.format(tc, result))
