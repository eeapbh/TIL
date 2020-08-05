'''
33
123
345
789
'''

# #1
# N, M = map(int, input().split())
# mylist = [0 for _ in range(N)]
# # mylist = [0]*N
# for i in range(N):
#     mylist[i] = list(map(int, input().split()))
#     print(mylist)
#
#
# #2
# N, M = map(int, input().split())
# mylist = []
# for i in range(N):
#     mylist.append(list(map(int, input().split())))
# print(mylist)
#
# #3
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

for i in range(N):
    for j in range(M):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)

# # 0으로 초기화
# N = 3 #행
# M = 4 #행
# # v = [[0 for _ in range(N)] for _ in range(M)]
# v = [[0] * N for _ in range(M)]
# print(v)