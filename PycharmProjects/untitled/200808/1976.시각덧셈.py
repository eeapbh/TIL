import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
for tc in range(1, t+1):
    s1, b1, s2, b2 = map(int, input().split())
    S = s1+s2
    B = b1+b2
    if S>=13:
        S = S-12
    if B >=60:
        B = B-60
        S += 1
    print(f'#{tc} {S} {B}')
