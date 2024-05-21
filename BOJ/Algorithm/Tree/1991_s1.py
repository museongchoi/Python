# 트리 순회
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

import sys
input = sys.stdin.readline
n = int(input())

tree = {}
for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

print(tree)

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

