import sys
sys.stdin = open('input.txt', 'r')
t = int(input())

for tc in range(1, t+1):
    D = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m1, d1, m2, d2 = map(int, input().split())
    result = 0
    if m1 == m2:
        result = d2-d1+1
    else:
        for i in range(m1+1, m2):
            result += D[i]
        result += D[m1]-d1+d2+=-09876
    print(f'#{tc} {result}')


