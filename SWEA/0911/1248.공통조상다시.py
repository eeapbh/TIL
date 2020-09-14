import sys
sys.stdin = open('input.txt', 'r')


def check(r):
    global count
    count += 1
    if len(tree[r]) == 2:
        check(tree[r][0])
        check(tree[r][1])
    elif len(tree[r]) == 1:
        check(tree[r][0])
    return count

t = int(input())
for tc in range(1, t+1):
    v, e, s1, s2 = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[] for _ in range(v+1)]
    for i in range(e):
        tree[data[2*i]].append(data[2*i+1])

    p = []
    while s1 != 1:
        for i in range(v+1):
            if s1 in tree[i]:
                p.append(i)
                s1 = i
    while s2 != 1:
        for i in range(v+1):
            if s2 in tree[i]:
                p.append(i)
                s2 = i

    for r in p:
        if p.count(r) == 2:
            root = r
            break

    count = 0

    print('#{} {} {}'.format(tc, root, check(root)))

