import sys
sys.stdin = open('input.txt', 'r')

# n = int(input())
# # 1 동
# # 2 서
# # 3 남
# # 4 북
# # 12 중에 젤큰거 곱하기 34중에 젤큰거 160곱하기 50 = 전체 테두리
# # 12중에 2번나온거 중에 처음 곱하기 34중에 2번나온거중에 두번째 60 곱하기 20
# save ={1:[], 2:[], 3:[], 4:[]}
# saveS = []
# start = 0
# for i in range(6):
#     s, l = map(int, input().split())
#     save[s].append(l)
#     if i == 0:
#         start = s
#
# # print(save)
# r = max(save[1])
# if r < max(save[2]):
#     r = max(save[2])
# c = max(save[3])
# if c < max(save[4]):
#     c = max(save[4])
#
# # print(r*c)
# sr = sc = 0
# for i in range(1, 3):
#     if len(save[i]) == 2:
#         if start == 3 or start==4:
#             sr = save[i][0]
#         else:
#             sr = save[i][1]
#
# for i in range(3, 5):
#     if len(save[i]) == 2:
#         if start==3 or start == 4:
#             sc = save[i][1]
#         else:
#             sc = save[i][0]
#
# # print( sr*sc)
# print((r*c - sr*sc)*n)
#
# K = int(input())

pos = []
for i in range(6):
    dir, length = map(int, input().split())
    pos.append(length)

big = 0
small = 0
for i in range(6):
    tmp = pos[i] * pos[(i + 1) % 6]
    if big < tmp:
        big = tmp
        idx = i
small = pos[(idx + 3) % 6] * pos[(idx + 4) % 6]
print(K * (big - small))
