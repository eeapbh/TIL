import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    t = int(input())
    result = []
    arr = [list(input()) for _ in range(100)]
    for m in range(1,100):

        for i in range(100):
            for j in range(100-m+1):
                row = ''
                col = ''
                for a in range(m):
                    row += arr[i][j+a]
                    col += arr[j+a][i]
                if row == row[::-1]:
                    result.append(len(row))
                if col == col[::-1]:
                    result.append(len(col))
    max_num = max(result)


    print('#{} {}'.format(t, max_num))





