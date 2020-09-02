for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    save = []
    for i in range(100):
        for j in range(100):
            check1 = []
            check2 = []
            for k in range(100):
                check1 = arr[i][j:k+1]
                check2 = check1[::-1]
                if check1 == check2:
                    save.append(len(check1))

    arr2 = list(zip(*arr))
    for i in range(100):
        for j in range(100):
            check1 = []
            check2 = []
            for k in range(100):
                check1 = arr2[i][j:k + 1]
                check2 = check1[::-1]
                if check1 == check2:
                    save.append(len(check1))

    print('#{} {}'.format(tc, max(save)))