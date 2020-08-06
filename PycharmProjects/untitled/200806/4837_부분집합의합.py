import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    # 길이 n 합 k
    count = 0
    N = 12
    sub_lists = []
    for i in range(1<<N):
        sub_list = []
        for j in range(N):
            if i & (1<<j):
                sub_list.append(j+1)
        sub_lists.append(sub_list)

    for sub_li in sub_lists:
        if len(sub_li) == n:
            if sum(sub_li) == k:
                count += 1

    print(f'#{tc} {count}')


