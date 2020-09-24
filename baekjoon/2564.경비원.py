import sys
sys.stdin = open('input.txt', 'r')

r, c = map(int, input().split())
n = int(input())
# 1 북
# 2 남
# 3 서
# 4 동

save = []
for i in range(n+1):
    x = y = 0
    ewsn, d = map(int, input().split())
    if ewsn == 1:
        x = 0
        y = d
    elif ewsn == 2:
        x = c
        y = d
    elif ewsn == 3:
        x = d
        y = 0
    elif ewsn == 4:
        x = d
        y = r

    save.append((x, y, ewsn))

# 동근이 좌표
Sx, Sy, Sewsn= save[n]
total = 0

for i in range(n):
    x, y, ewsn= save[i]

    # 같은 선에있으면
    if x == Sx:
        total += abs(Sy-y)
        continue
    if y == Sy:
        total += abs(Sx-x)
        continue

    # 다른 선에 있는데 동근이가 북남에 있을때
    if Sewsn <=2:
        if ewsn <=2:
            total += min(c+Sy+y, c-Sy-y+ 2*r)
        else:
            total += abs(Sx-x)+abs(Sy-y)
    # 다른 선에 있는데 동근이가 동서중에 있을때
    if Sewsn >2:
        if ewsn >2:
            total += min(r+Sx+x, r-Sx-x+ 2*c)
        else:
            total += abs(Sx-x)+abs(Sy-y)

print(total)





