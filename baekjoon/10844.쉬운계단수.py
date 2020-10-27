n = int(input())
dp = [[0]*10 for _ in range(n)]
dp[0] = [1 for _ in range(10)]
for i in range(1, n):
    for j in range(10):
        if 0 <= j <= 8:
            dp[i][j] += dp[i-1][j+1]
        if 1 <= j <= 9:
            dp[i][j] += dp[i-1][j-1]
rs = sum(dp[n-1])-dp[n-1][0]
print(rs%1000000000)