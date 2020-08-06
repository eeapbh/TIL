import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []
    for i in range(N//2):
        result.append(max(numbers))
        numbers.remove(max(numbers))
        result.append(min(numbers))
        numbers.remove(min(numbers))

    print(f'#{tc} ', end = '')
    for j in range(10):
        print(result[j], end = ' ')
    print()

