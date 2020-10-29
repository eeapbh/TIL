import sys
sys.stdin = open('input.txt', 'r')

def check(arr):
    tmp = sorted(arr)
    run_cnt = 0
    tri_cnt = 0
    for i in range(len(tmp) - 1):
        if tmp[i] == tmp[i + 1]:
            run_cnt += 1
        else:
            run_cnt = 0
        if tmp[i] + 1 == tmp[i + 1]:
            tri_cnt += 1
        else:
            tri_cnt = 0
        if run_cnt == 2 or tri_cnt == 2:
            return 1
    return 0
for tc in range(1, int(input()) + 1):
    nums = list(map(int, input().split()))
    p1 = sorted(nums[::2])
    p2 = sorted(nums[1:][::2])
    res = 0
    for k in range(3, 7):
        res_p1 = check(p1[:k])
        res_p2 = check(p2[:k])
        if res_p1 == 1:
            res = 1
            break
        if res_p2 == 1:
            res = 2
            break
    print('#{} {}'.format(tc, res))