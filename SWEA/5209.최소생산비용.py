import sys
sys.stdin = open('input.txt', 'r')
def check(bit, idx, total):

    global min
    if bit == (1<<n)- 1:
        if total < min:
            min = total
        return
    if total > min:
        return
    for i in range(n):
        if bit & (1<<i):
            continue
        check(bit | 1<<i, idx+1, total +arr[idx][i])


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min = 987654
    check(0, 0, 0)
    print(min)