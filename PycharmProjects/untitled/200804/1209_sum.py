import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    t = int(input())
    dagak1 = 0
    dagak2 = 0
    result = []
    lists = []
    garo = []
    saero = 0
    s_list =[]
    for i in range(100):
        numbers = list(map(int, input().split()))
        lists.append(numbers)

    for j in lists:
        garo.append(sum(j))
    result.append(max(garo))
    # print(f'garo {max(garo)}')

    for k in range(100):
        dagak1 += lists[k][k]
        dagak2 += lists[k][99-k]
    result.append(dagak1)
    result.append(dagak2)
    # print(f'dagak2 {dagak2}')
    # print(f'dagak1 {dagak1}')

    for m in range(100):
        saero=0
        for n in range(100):
            saero += lists[n][m]
        s_list.append(saero)
        result.append(max(s_list))
    # print(f'saero {max(s_list)}')

    print(f'#{t} {max(result)}')