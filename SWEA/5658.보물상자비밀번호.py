import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    info = input()
    save = set()

    # for _ in range(n//4):
    #     for i in range(0, n, n//4):
    #         tmp = info[i:i + (n//4)]
    #         save.add(tmp)
    #     tmp = info[1:n]+info[0]
    #     info = tmp[:]
    # for s in save:
    #     number.append(int(s, 16))
    # number.sort(reverse=True)
    #
    # print('#{} {}'.format(tc, number[k-1]))
    for _ in range(n//4):
        for i in range(0, n, n//4):
            save.add(int(info[i:i+(n//4)], 16))

        info = info[1:n]+info[0]
    number = list(save)
    number.sort(reverse=True)


    print('#{} {}'.format(tc, number[k-1]))

