import sys
sys.stdin = open('input.txt', 'r')

r, c = map(int, input().split())
n = int(input())
row = [0]
col = [0]
r1 = []
r2 = []
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        col.append(b)
    else:
        row.append(b)
row.append(r)
col.append(c)
row.sort()
col.sort()

for i in range(len(row)-1):
    r1.append(row[i+1] - row[i])

for i in range(len(col)-1):
    r2.append(col[i+1] - col[i])

print(max(r1)*max(r2))
