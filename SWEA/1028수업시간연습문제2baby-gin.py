from itertools import permutations

import sys
sys.stdin = open('input.txt', 'r')

def run(arr):
    for i in range(2):
        if arr[i] + 1 == arr[i+1]:
            return 1
    else:
        return -1

def triplet(arr):
    if arr[0] == arr[1] and arr[1] == arr[2]:
        return 1
    else:
        return -1



def check(perms):
    for p in perms:
        a = p[:3]
        b = p[3:6]
        if run(a) + run(b) == 2 or run(a) + triplet(b) == 2 or triplet(a) + run(b) == 2 or triplet(a) + triplet(b) == 2:
            return 1
        else:
            return -1




def perm(idx):
    if idx == n:
        tmp = sel
        perms.append(tmp)
        return
    for i in range(n):
        if not visited[i]:
            sel[idx] = line[i]
            visited[i] = 1
            perm(idx+1)
            visited[i] = 0
N = int(input())
for i in range(N):
    line = list(map(int, input().split()))
    n = len(line)
    sel = [0] * n
    visited = [0] * n
    perms = []
    perm(0)

    if check(perms) == 1:
        print('맞음')
    else:
        print('아님')