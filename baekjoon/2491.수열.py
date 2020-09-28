import sys
sys.stdin = open('input.txt', 'r')

# n = int(input())
# arr = list(map(int, input().split()))
# cnt = 0
# check = 0
# same = 0
# save = []
#
# for i in range(n-1):
#     if arr[i] == arr[i+1]:
#         cnt += 1
#         same += 1
#         save.append(cnt+1)
#         continue
#     if arr[i] < arr[i+1]:
#         if check == 0 or check == 1:
#             cnt += 1
#             check = 1
#         else:
#             cnt = same
#             same = 0
#             cnt += 1
#             check = 1
#
#     if arr[i] > arr[i+1]:
#         if check == 0 or check == -1:
#             cnt += 1
#             check = -1
#         else:
#             cnt = same
#             same = 0
#             cnt += 1
#             check = -1
#
#     save.append(cnt+1)
# print(save)
# print(max(save))
def check(arr):
    global ans
    cnt = 1
    for i in range(n-1):
        if arr[i]<=arr[i+1]:
            cnt += 1
        else:
            cnt = 1

        if ans < cnt:
            ans = cnt


n = int(input())
arr = list(map(int, input().split()))
ans = 1
check(arr)
check(arr[::-1])
print(ans)





