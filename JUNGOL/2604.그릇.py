line = input()
tmp = line[0]
l = len(line)
ans = 10
for i in range(1, l):
    if line[i] == tmp:
       ans += 5
    else:
        ans += 10
        tmp = line[i]

print(ans)


