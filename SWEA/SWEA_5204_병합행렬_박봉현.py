import sys
sys.stdin = open('input.txt', 'r')

def merge(left, right):
    global ans
    result = [0]*(len(left) + len(right))
    idx = li = ri = 0
    if left[-1] > right[-1]:
        ans += 1
    while len(left) > li and len(right) > ri:
        if left[li] <= right[ri]:
            result[idx] = left[li]
            li += 1
            idx += 1
        else:
            result[idx] = right[ri]
            ri += 1
            idx += 1
    while len(left) > li:
        result[idx] = left[li]
        li += 1
        idx += 1
    while len(right) > ri:
        result[idx] = right[ri]
        li += 1
        idx += 1

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0












#
# def merge(arr):
#     cnt = 0
#     length = len(arr)
#     if length <= 1:
#         return arr, cnt
#     else:
#         left, leftCnt = merge(arr[:length//2])
#         right, rightCnt = merge(arr[length//2:])
#
#         result = []
#         leftIdx = rightIdx = 0
#         check = 0
#         for _ in range(length):
#             if leftIdx == len(left):
#                 result.append(right[rightIdx])
#                 rightIdx += 1
#             elif rightIdx == len(right):
#                 result.append(left[leftIdx])
#                 leftIdx += 1
#                 check = 1
#             elif left[leftIdx] <= right[rightIdx]:
#                 result.append(left[leftIdx])
#                 leftIdx += 1
#             else:
#                 result.append(right[rightIdx])
#                 rightIdx += 1
#         cnt = leftCnt + rightCnt
#         if check:
#             cnt += 1
#         return result, cnt
# def sorted_merge(arr):
#     sorted_arr, cnt = merge(arr)
#     return sorted_arr[n//2], cnt