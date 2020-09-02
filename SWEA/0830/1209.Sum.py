import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_r = sum_c = 0
    rli = []
    cli = []
    degak1 = degak2 = 0

    for i in range(100):
        for j in range(100):
            sum_r += arr[i][j]
            sum_c += arr[j][i]
            if i==j:
                degak1 += arr[i][j]
            if i+j == 99:
                degak2 += arr[i][j]
        rli.append(sum_r)
        cli.append(sum_c)
        sum_r = 0
        sum_c = 0
    print('#{} {}'.format(tc, max(max(rli), max(cli), degak1, degak2)))