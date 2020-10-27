import sys
import copy
sys.stdin = open('input.txt', 'r')


def powerset(idx):
    if idx == m:
        tmp = []
        for s in range(m):
            if sel[s]:
                tmp.append(food[s])

            tmp2 = copy.deepcopy(tmp)
        save.append(tmp2)
        return
    sel[idx] = 1
    powerset(idx + 1)
    sel[idx] = 0
    powerset(idx + 1)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    food = []
    home = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                home.append([i, j])
            if arr[i][j] >1:
                food.append([i, j])

    # print('food: {}'.format(food))
    m = len(food)
    sel = [0] * m
    save = []
    powerset(0)
    ans = []
    # print(save)
    for i in range(2**m-1):# 조합중에 하나 골르고
        result = 0
        for foods in save[i]:
            result += arr[foods[0]][foods[1]]
        # print(result)
        for h in home:
            minD = 100000
            for s in save[i]:
                d = abs(h[0] - s[0]) + abs(h[1] - s[1])
                if d < minD:
                    minD = d
                    f = s[:]
            result += minD
        # print(f)

        ans.append(result)
    # print(ans)
    print("#{} {}".format(tc, min(ans)))


