import sys
sys.stdin = open('input.txt', 'r')

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr)//2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])
    return merge(left, right)

def merge(left, right):
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result



t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    print('#{} {} {}'.format(tc, merge_sort(arr)[n//2], cnt))










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