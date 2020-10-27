import sys
sys.stdin = open('input.txt','r')

# A F , B D, C E,
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dic = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
m = 0
for i in range(6):
    result =[]
    st = arr[0][i]
    ed = arr[0][dic[i]]
    tmp = [1, 2, 3, 4, 5, 6]
    tmp.remove(st)
    tmp.remove(ed)
    result.append(max(tmp))
    for i in range(1, n):
        tmp = [1, 2, 3, 4, 5, 6]
        st = ed
        ed = arr[i][dic[arr[i].index(st)]]
        tmp.remove(st)
        tmp.remove(ed)
        result.append(max(tmp))
    s = sum(result)
    if m < s:
        m = s
print(m)