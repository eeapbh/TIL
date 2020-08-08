t = int(input())
for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    print(f'#{tc} {round(sum(numbers)/len(numbers))}')