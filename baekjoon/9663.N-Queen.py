def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]- row[i]) == x - i:
            return 0
    return 1

def dfs(x):
    global ans

    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x+1)

n = int(input())
row = [0]*n
ans = 0
dfs(0)
print(ans)