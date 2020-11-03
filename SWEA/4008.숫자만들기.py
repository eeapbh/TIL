import sys
# from itertools import permutations
sys.stdin = open('input.txt', 'r')
op_dict = {0: '+', 1: '-', 2:'*', 3:'/'}
def calc(op):
    ans = nums[0]
    for i in range(1, N):
        if op[i-1]== '+':
            ans = ans + nums[i]
        elif op[i-1]=='-':
            ans = ans -nums[i]
        elif op[i-1] == '*':
            ans = ans * nums[i]
        else:
            ans = int(ans/ nums[i])
    return ans


def permutation(idx, o):
    global minV, maxV
    if idx == N - 1:
        tmp = calc(o)

        minV = min(minV, tmp)
        maxV = max(maxV, tmp)
        print(o)
        return

    for i in range(len(op_cnt)):
        if op_cnt[i]:
            o[idx] = op_dict[i]
            op_cnt[i] -=1
            permutation(idx+1, o)
            op_cnt[i] += 1

for tc in range(1, int(input()) + 1):
    N = int(input())
    op_cnt = list(map(int, input().split()))
    nums = list(map(int, input().split()))


    minV = 987654321
    maxV = -987654321

    permutation(0, [0]*(N-1))

    print("#{} {}".format(tc, maxV-minV))
