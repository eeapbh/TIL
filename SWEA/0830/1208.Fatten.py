import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if max(arr) == min(arr):
            break
        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))
        arr[max_idx] -= 1
        arr[min_idx] += 1
    print('#{} {}'.format(tc, max(arr)- min(arr)))