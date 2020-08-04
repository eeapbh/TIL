#import sys
#sys.stdin = open("input.txt", "r")
# k = 한번충전으로 갈수있는 수
# m = 충전소 갯수
# n = 끝정류장 번호
# 최대한 갈수있는만큼 감-> 갔는데 충전소가 있다. 그럼 계쏙 진행
# 충전소가 없다?-> 그전에 충전을 해야함 ->거기로 이동
# 충전소가 없다? -> 그전에 충전을 해야함  가장먼 충전소로 ->그런데 그전에 충전소가없다. ->0
# 갈수있는 최대장소가 n을 넘어가는 시점에 반복문 종료
t = int(input())
for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    place = 0 #내가있는 장소
    result = 0
    while True:
        cnt = 0
        for i in range(place+k, -1, -1):
            if i >= n:
                place = i
                break
            if i in numbers:
                place = i
                break
            cnt += 1
        if place >= n:
            break
        if cnt >=k:
            result = 0
            break
        else:
            result += 1

    print(f'#{tc} {result}')

