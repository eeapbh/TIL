import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
def spin(x):
    if abs(n-x) == 2 or (n-x) == 0:
        if s == 1:
            tmp = arr[x].pop(7)
            arr[x].insert(0, tmp)
        else:
            tmp = arr[x].pop(0)
            arr[x].insert(7, tmp)
    else:
        if s == 1:
            tmp = arr[x].pop(0)
            arr[x].insert(7, tmp)
        else:
            tmp = arr[x].pop(7)
            arr[x].insert(0, tmp)
for tc in range(1, t+1):
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]
    for i in range(k):
        n, s = map(int, input().split()) # n번째바퀴가 s방향으로 도는지
        n = n-1
        # n극 0 s극 1
        # 0(화살표) 3(앞에꺼랑 만나는거) 6(뒤에꺼랑만나는거)
        # 1 시계방향  -1 반시계
        num = []
        # print(arr)
        if n == 0 or n== 1:
            for a in range(3):
                if arr[a][2] != arr[a + 1][6]:
                    if a not in num:
                        num.append(a)
                    if a + 1 not in num:
                        num.append(a + 1)
                else:
                    if a < n:
                        continue
                    else:
                        break

        elif n == 3 or n == 2:
            for a in range(3, 0, -1):
                if arr[a][6] != arr[a - 1][2]:
                    if a not in num:
                        num.append(a)
                    if a - 1 not in num:
                        num.append(a - 1)
                else:
                    if a > n:
                        continue
                    else:
                        break
        if n not in num:
            num.append(n)
        # print(f'{i}번째 돌아가는 바퀴다찾음\n{num}')
        for x in num:
            spin(x)
        # print(f'{i}번째 다돌림 \n{arr}')
    score = 0

    for i in range(4):
        jum = 2 ** i
        if arr[i][0] == 1:
            score += jum

    print('#{} {}'.format(tc, score))
