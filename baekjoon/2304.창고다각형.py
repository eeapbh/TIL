n = int(input())

arr = [0] * 1001
max_h = 0
max_idx = 0
for _ in range(n):
    idx, height = map(int, input().split())
    arr[idx] = height
    if max_h < height:
        max_h = height
        max_idx = idx
curr_h = 0
ans = 0
for i in range(max_idx + 1):
    if arr[i] > curr_h:
        curr_h = arr[i]
    ans += curr_h

curr_h = 0
for i in range(1000, max_idx, -1):
    if arr[i] > curr_h:
        curr_h = arr[i]
    ans += curr_h
print(ans)