t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    spin90 = []
    spin180 = []
    spin270 = []
    tmp = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(arr[j][i])
        tmp.reverse()
        spin90.append(tmp)

    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(spin90[j][i])
        tmp.reverse()
        spin180.append(tmp)

    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(spin180[j][i])
        tmp.reverse()
        spin270.append(tmp)
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(spin90[i][j], end='')
        print(end=' ')
        for j in range(n):
            print(spin180[i][j], end='')
        print(end=' ')
        for j in range(n):
            print(spin270[i][j], end='')
        print()
