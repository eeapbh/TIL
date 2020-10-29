import sys
sys.stdin = open('input.txt', 'r')

from itertools import permutations

def check(arr):
    perms = list(permutations(arr, 3))
    for perm in perms:
        if perm[0] == perm[1] and perm[1] == perm[2]:
            return 1
        if perm[0] + 1 == perm[1] and perm[1] + 1 == perm[2]:
            return 1
    return -1


t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    a = []
    b = []

    for i in range(6):
        a.append(arr[2*i])
        b.append(arr[2*i + 1])
    for i in range(3, 7):
        rs = [0, 0]
        p1 = a[0:i]
        p2 = b[0:i]
        rs[0] = (check(p1))
        if rs.count(1) == 1:
            print('#{} {}'.format(tc, rs.index(1)+1))
            break
        rs[1] = (check(p2))
        if rs.count(1) == 1:
            print('#{} {}'.format(tc, rs.index(1)+1))
            break

        else:
            if i == 6:
                print('#{} {}'.format(tc, 0))



    #
    #     if rs.count(1) == 2:
    #         print('#{} {}'.format(tc, 0))
    #         break
    #     elif rs.count(1) == 1:
    #         print('#{} {}'.format(tc, rs.index(1)+1))
    #         break
    # else:
    #     print('#{} {}'.format(tc, 0))