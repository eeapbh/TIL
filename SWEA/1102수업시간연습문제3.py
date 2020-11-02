arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
n = 12
tree = [[0]*3 for _ in range(n+2)]

for i in range(n):
    p, c = arr[2*i], arr[2*i + 1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p

def preorder(node):
    if node:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node:
        inorder(tree[node][0])
        print(node, end=' ')
        inorder(tree[node][1])

def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=' ')
print(tree)
preorder(1)
print()
inorder(1)
print()
postorder(1)