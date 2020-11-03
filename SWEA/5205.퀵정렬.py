import sys
sys.stdin = open('input.txt', 'r')

def quick(arr, l, r):
    if l<r:
        p = partition(arr, l, r)
        if p == n//2:
            return
        elif p > n//2:
            quick(arr, l, p-1)
        else:
            quick(arr, p+1, r)

def partition(arr, l, r):
    pivot = (l+r) // 2
    while l<r:
        while(arr[l] < arr[pivot] and l<r):
            l += 1
        while(arr[r] >= arr[pivot] and l<r):
            r -= 1
        if l<r:
            if l == pivot:
                pivot = r
            arr[l], arr[r] = arr[r], arr[l]
    arr[pivot], arr[r] = arr[r], arr[pivot]
    return r

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quick(arr, 0, n-1)
    print('#{} {}'.format(tc, arr[n//2]))