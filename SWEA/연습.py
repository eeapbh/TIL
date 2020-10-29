import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N): # 신청서를 튜플로 lst에 저장
        lst.append(tuple(map(int, input().split())))
    lst.sort(key=lambda e : e[1]) # 빨리 끝나는 순으로 정렬
    print(lst)
    result = 0
    work_done = 0 # 작업 끝난 시간
    while lst:
        start_time, end_time = lst.pop(0)
        if start_time >= work_done: # 작업 가능
            result += 1
            work_done = end_time # 작업 끝나는 시간 갱신
    print('#{} {}'.format(test_case, result))