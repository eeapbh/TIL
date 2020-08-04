t = int(input())
for i in range(1, t+1):
    n = int(input())
    number = list(map(int, input().split()))
    print(f'#{i} {max(number)- min(number)}')