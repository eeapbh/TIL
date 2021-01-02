line = input()
l = len(line)
tmp = []
ans1 = 0
ans2 = 0
for i in range(l-2):
    tmp = line[i:i+3]
    if ''.join(tmp) == "KOI":
        ans1 += 1

    if ''.join(tmp) == "IOI":
        ans2 += 1

print(ans1)
print(ans2)
