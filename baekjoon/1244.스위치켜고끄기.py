import sys
sys.stdin = open('input.txt', 'r')

# n = int(input())
# tmp = list(map(int, input().split()))
# arr = [5]
# arr.extend(tmp)
#
# std = int(input())
# for i in range(std):
#     d = 0
#     s, num = map(int, input().split())
#     if s == 1:
#         for i in range(1, n):
#             if i>0 and i%num == 0:
#                 if arr[i]:
#                     arr[i] = 0
#                 else:
#                     arr[i] = 1
#
#     else:
#         st = num
#         ed = num
#         while arr[num-d] == arr[num+d] and 1<=num-d<n+1 and 1<=num+d<n+1:
#             d += 1
#             st = num-d
#             ed = num+d
#
#
#         # print(st)
#         # print(ed)
#         for j in range(st, ed+1):
#             if arr[j]:
#                 arr[j] = 0
#             else:
#                 arr[j] = 1
#     # print(arr)
# for k in range(1, n+1):
#     print(arr[k], end=' ')

# 0 1 0 1 0 0 0 1
# 0 1 1 1 0 1 0 1
# 1 0 0 0 1 1 0 1
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 3)
s = int(input())

for i in range(s):

    gender, num = map(int, input().split())
    if gender == 1:
        for j in range(1, n+1):
            if j % num == 0:
                if arr[j]:
                    arr[j] = 0
                else:
                    arr[j] = 1
    else:
        left = right = num
        while 1:
            left -= 1
            right += 1
            if left <1 or right > n or arr[left] != arr[right]:
                left += 1
                right -= 1
                break

        for a in range(left, right+1):
            if arr[a]:
                arr[a] = 0
            else:
                arr[a] = 1

for i in range(1, n+1):
    print(arr[i], end=' ')
    if i % 20 == 0:
        print()



