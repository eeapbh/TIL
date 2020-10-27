n = int(input())
tree = [[] for _ in range(n+1)]

for i in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
# print(tree)
q = [1]
ans = {}
check = [0 for _ in range(n+1)]
while len(q)>0:
    parent = q.pop(0)
    for i in tree[parent]:
        if not check[i]:
            ans[i] = parent
            q.append(i)
            check[i] = 1
# print(ans)
for i in range(2, n+1):
    print(ans[i])