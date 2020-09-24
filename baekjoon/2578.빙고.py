import sys
sys.stdin = open('input.txt', 'r')

def check(num):
    cnt = 0
    for row in visit:
        if sum(row) == 5:
            cnt += 1

    visit2 = list(zip(*visit))
    for col in visit2:
        if sum(col) == 5:
            cnt += 1


    dae = []
    for i in range(5):
        r = c = i
        dae.append(visit[r][c])
    if sum(dae) == 5:
        cnt += 1

    dae2 = []
    for i in range(4, -1, -1):
        r = i
        c = 4-i
        dae2.append(visit[r][c])
    if sum(dae2) == 5:
        cnt += 1

    if cnt >= 3:
        return call.index(num)+1

def find():
    for c in call:
        for i in range(5):
            for j in range(5):
                if arr[i][j] == c:
                    visit[i][j] = 1
                    result = check(c)
                    if result:
                        return result

arr = [list(map(int, input().split())) for _ in range(5)]
save = []
call = []
visit = [[0]*5 for _ in range(5)]
for _ in range(5):
    call.extend(list(map(int, input().split())))

print(find())
