import sys

sys.stdin = open('input.txt', 'r')
t = int(input())

for tc in range(1, t + 1):
    hab = 0
    hab_list = []
    lists = []
    n, m = map(int, input().split())
    lists = [list(map(int, input().split())) for i in range(n)]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            for s in range(m):
                for k in range(m):
                    hab += lists[i + s][j + k]
            hab_list.append(hab)
            hab = 0

    print(f'#{tc} {max(hab_list)} ')


