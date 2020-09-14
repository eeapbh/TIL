import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    arr = [[]]
    for i in range(1, n+1):
        arr.append(list(input().split()))
        if len(arr[i]) == 4:
            arr[i][2] = int(arr[i][2])
            arr[i][3] = int(arr[i][3])
        else:
            arr[i][1] = int(arr[i][1])

    def cal(v):
        if len(arr[v]) == 2:
            return arr[v][1]
        else:
            l = cal(arr[v][2])
            r = cal(arr[v][3])

            if arr[v][1] == '+':
                return l+r
            if arr[v][1] == '-':
                return l-r
            if arr[v][1] == '*':
                return l*r
            if arr[v][1] == '/':
                return l/r

    print('#{} {}'.format(tc, int(cal(1))))
