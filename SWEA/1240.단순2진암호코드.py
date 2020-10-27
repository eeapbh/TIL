import sys
sys.stdin = open('input.txt', 'r')

dic = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
       '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

t = int(input())
def find(arr):
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if arr[i][j] == '1':
                sx, sy = i, j - 55
                return sx, sy

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    sx, sy = find(arr)
    pwCode = []
    for i in range(sy, sy+56, 7):
        tmp =[]
        tmp += arr[sx][i:i+7]
        num = "".join(tmp)
        pwCode.append(dic[num])

    # print(pwCode)
    firstSum = sum(pwCode)
    for i in range(7):
        if i % 2 == 0:
            pwCode[i] = 3 * pwCode[i]
    # print(pwCode)
    if sum(pwCode) % 10 == 0:
        print('#{} {}'.format(tc, firstSum))
    else:
        print('#{} {}'.format(tc, 0))