import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
for tc in range(1, t+1):
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    N, num = map(int, input().split())
    sums = []
    sum = 0
    result = 0
    for i in range(N):
        a, b, c = map(int, input().split())
        sum = 0.35 * a + 0.45 * b + 0.2 *c
        sums.append(sum)
    result = sums[num-1]
    sums.sort(reverse=True)
    length = N//10
    for j in range(N):
        if sums[j] == result:
            print(f'#{tc} {grade[j//length]}')
