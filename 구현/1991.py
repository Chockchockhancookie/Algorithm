def preorder(txt):
    if txt != ".":
        print(txt, end="")
        preorder(tree[txt][0])
        preorder(tree[txt][1])


def inorder(txt):
    if txt != ".":
        inorder(tree[txt][0])
        print(txt, end="")
        inorder(tree[txt][1])


def postorder(txt):
    if txt != ".":
        postorder(tree[txt][0])
        postorder(tree[txt][1])
        print(txt, end="")


n = int(input())

tree = {}
for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")
