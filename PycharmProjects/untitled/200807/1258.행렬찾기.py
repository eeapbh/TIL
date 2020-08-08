import sys
sys.stdin = open('input.txt', 'r')


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 왼쪽 꼭지점을 찾는다.
    # 왼쪽꼭지점부터 열을 +1 하면서 countI 0이나오면 count는 다른곳에저장
    # 왼쪽꼭지점부터 행을 +1 하면서 countJ . 0이나오면 count 는 ㄴ다른곳에 저장
    # 꼭지점부터 (countI, countJ)까지 0으로 바꿈
    # 다시처음부터

    result = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                countI = 0
                countJ = 0
                while arr[i][j + countJ] != 0:
                    countJ += 1
                while arr[i + countI][j] != 0:
                    countI += 1
                for x in range(countI):
                    for y in range(countJ):
                        arr[i + x][j + y] = 0
                result.append((countI, countJ))
    print(f'#{tc}', len(result), *sum(sorted(result, key=lambda x: (x[0] * x[1], x[0])), ()))


