for tc in range(1, 11):
    V, E = map(int, input().split())
    line = [[0] * (V + 1) for _ in range(V + 1)]
    infos = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        s = infos[i]
        e = infos[i + 1]
        line[e][s] = 1
    res = []
    while True:
        if len(res) == V:
            break
        pri_col = []
        for c in range(1, len(line)):
            if 1 not in line[c] and c not in res:
                pri_col.append(c)
        for c in pri_col:
            res.append(c)
            for r in range(len(line)):
                line[r][c] = 0
    print('#{}'.format(tc), end=" ")
    for i in res:
        print(i, end =" ")
    print()