def check(idx, hab):
    global total
    if len(total) >0:
        if hab > min(total):
            return
    if idx == n:
        total.append(hab)
        return

    for i in range(n):
        if vist[i] == 0:
            save[idx] = arr[idx][i]
            vist[i] = 1
            check(idx+1, hab +save[idx])
            vist[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    save = [0]*n    # 값을 저장
    vist = [0]*n    # 행에서 골른 idx를 표시
    total = []
    check(0, 0)
    print('#{} {}'.format(tc, min(total)))