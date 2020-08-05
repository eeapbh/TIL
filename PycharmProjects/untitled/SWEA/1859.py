import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
for tc in range(1, t+1):
    length = int(input())
    numbers = list(map(int, input().split()))
    max = numbers[-1]
    sum = 0
    for i in range(len(numbers)-1, -1, -1):
        if max > numbers[i]:
            sum += max - numbers[i]
        else:
            max = numbers[i]
    print(f'#{tc} {sum}')


