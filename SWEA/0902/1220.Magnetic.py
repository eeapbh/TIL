for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # N극 1  S극 2 
    # 위에가 N극 아래가 S극
    # 상하 탐색을 함
    # 자신이 n극이면 아래 탐색 아래가 0이면 내려감 nx >n 이면 0으로 바꿈
    ans = 0
    for i in range(n):
        state = 1
        for j in range(n):
            
