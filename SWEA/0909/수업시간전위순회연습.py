v = int(input())
data = list(map(int, input().split()))
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

arr = [[0]*(v+1) for _ in range(v+1)]

for i in range(0, len(data), 2):
    arr[data[i]][data[i+1]] = 1



