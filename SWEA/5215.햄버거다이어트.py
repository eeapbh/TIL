from itertools import combinations
import sys
sys.stdin = open('input.txt', 'r')
# t = int(input())
# for tc in range(1, t+1):
#     n, l = map(int, input().split())
#
#     arr = []
#     save = []
#     for i in range(n):
#         t, j = map(int, input().split())
#         arr.append((t, j))
#     # maxscore = 0
#     for i in range(1, n+1):
#         tmp = list(combinations(arr, i))
#
#         for t in tmp:
#
#             kal = 0
#             score = 0
#             for s in t:
#                 kal += s[1]
#                 score += s[0]
#                 if kal > l:
#                     break
#
#             else:
#                 save.append((score, kal))
#
#     save.sort()
#     # print(save)
#     print('#{} {}'.format(tc, save[-1][0]))

# 비트연산
# for tc in range(1, int(input())+1):
#     n, l = map(int, input().split())
#     score, calorie = [], []
#     for _ in range(n):
#         s, c = map(int, input().split())
#         score.append(s)
#         calorie.append(c)
#     ans = 0
#     for i in range(1<<n):
#         sum_score = 0
#         sum_calorie = 0
#         for j in range(n):
#             if i & (1<<j):
#                 sum_calorie += calorie[j]
#                 sum_score += score[j]
#         if sum_calorie <= l:
#             ans = max(ans, sum_score)
#     print('#{} {}'.format(tc, ans))


# 재귀
# def cook(idx):
#     global ans
#     if idx >= n:
#         sum_score = 0
#         sum_calorie = 0
#         for i in range(n):
#             if sel[i]:
#                 sum_score += score[i]
#                 sum_calorie += calorie[i]
#         if sum_calorie <= l:
#             ans = max(ans, sum_score)
#         return
#
#     # 재료를 뽑고가고
#     sel[idx] = True
#     cook(idx+1)
#     # 재료를 안뽑고가고
#     sel[idx] = False
#     cook(idx+1)
#
# for tc in range(1, int(input())+1):
#     n, l = map(int, input().split())
#     score, calorie = [], []
#     for _ in range(n):
#         s, c = map(int, input().split())
#         score.append(s)
#         calorie.append(c)
#     ans = 0
#     sel = [0]*n
#     cook(0)
#     print('#{} {}'.format(tc, ans))

# 백트레킹
def cook(idx, sum_score, sum_calorie):
    global ans
    if sum_calorie > l:
        return
    if idx == n:
        if sum_score > ans:
            ans = sum_score
        return
    #재료를 뽑고가고
    cook(idx + 1, sum_score + score[idx], sum_calorie + calorie[idx])
    #재룔를 안뽑고 가고
    cook(idx + 1, sum_score, sum_calorie)

for tc in range(1, int(input())+1):
    n, l = map(int, input().split())
    score, calorie = [], []
    for _ in range(n):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)
    ans = 0
    sel = [0]*n
    cook(0, 0, 0)
    print('#{} {}'.format(tc, ans))