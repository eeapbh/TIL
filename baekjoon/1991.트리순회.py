import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [[] for _ in range(n+1)]
dic = {}
for i in range(n):
    p, l, r = input().split()
    dic[p] = [l, r]

def preorder(A):
    if A == '.':
        return
    child = dic[A]
    print(A, end='')
    preorder(child[0])
    preorder(child[1])

def inorder(A):
    if A == '.':
        return
    child = dic[A]

    inorder(child[0])
    print(A, end='')
    inorder(child[1])

def postorder(A):
    if A == '.':
        return
    child = dic[A]

    postorder(child[0])
    postorder(child[1])
    print(A, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')