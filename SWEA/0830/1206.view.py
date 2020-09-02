import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2,n-2):
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            cnt += arr[i] - max(arr[i-1], arr[i-2], arr[i+2], arr[i+1])
    print('#{} {}'.format(tc, cnt))
