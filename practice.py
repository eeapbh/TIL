#import sys
#sys.stdin=open("input.txt","r")
t = int(input())
for tc in range(1, t+1):
    k,n,m=map(int, input().split())
    add = list(map(int, input().split()))
    # 1. 내 현재 위치에서 최대한 갈수있는 거리안에 충전소가 없으면 그냥 끝
    # 2. 내가 갈수있는 범위 내에 충전소가 있으면 그중 가장 먼거리에 있는 충전소로 이동
    # 3. 최종적으로 n에 도착하면 충전횟수를 출력
    place=0
    result=0
    while True :
        cnt=0
        for i in range(place+k)[::-1]:
            if i in add :
                place=i
                break
            cnt+=1
        if cnt>=k:
            result=0
            break
        else:
            result+=1
        if place>=n:
            break
        print(place,result)
        print('--------------------------')
    print(f'#{tc} {result}')

                
                    
  #  remember = K
#    count = 0
  #  for j in range(N+1):
 #       if j in add:
 #           if j + remember < N:
 #               remember += K
 #               count += 1
 #       remember = remember - 1
 #       if remember == 0:
#            count = 0
 #           break
#    print(f'#{i} {count}')~
