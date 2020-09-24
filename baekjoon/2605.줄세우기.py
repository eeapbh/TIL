n = int(input())
info = list(map(int, input().split()))

tmp = [1]
for i in range(2, n+1):
    tmp.insert(i-1-info[i-1], i)
print(*tmp)


