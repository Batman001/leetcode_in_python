# -*- coding:utf-8 -*-
from btree.TreeNode import CreateTree


def pre_order(root):
    if not root:
        return
    print(root.val, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def preorder_(root):
    stack = [root]

    while stack:
        root = stack.pop()
        print(root.val, end=" ")
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)


def pre_order_(root):
    stack = [root]
    while stack:
        root = stack.pop()
        print(root.val, end=' ')

        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val, end=' ')
    in_order(root.right)


def inorder_(root):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        if stack:
            root = stack.pop()
            print(root.val, end=" ")
            root = root.right


def in_order_(root):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            print(root.val, end=' ')
            root = root.right


def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=' ')


def postorder_(root):
    stack = [root]
    reverse_stack = []

    while stack:
        root = stack.pop()
        reverse_stack.append(root)

        if root.left:
            stack.append(root.left)

        if root.right:
            stack.append(root.right)

    while reverse_stack:
        cur_node = reverse_stack.pop()
        print(cur_node.val, end=' ')


def post_order_(root):
    stack = [root]
    reverse_stack = []
    while stack:
        root = stack.pop()
        reverse_stack.append(root)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

    while reverse_stack:
        cur_node = reverse_stack.pop()
        print(cur_node.val, end=' ')


if __name__ == "__main__":
    array_string = " [3, 5, 1,6, 2,0, 8,null,null,7,4]"
    tree = CreateTree.create_tree_by_string(array_string)
    print("前序遍历结果为:")
    pre_order(tree)
    print()
    print("非递归前序遍历结果为：")
    pre_order_(tree)
    print()

    print("中序遍历结果为:")
    in_order(tree)
    print()
    print("非递归中序遍历结果为：")
    in_order_(tree)
    print()

    print("后序遍历结果为：")
    post_order(tree)
    print()

    print("非递归后序遍历结果为：")
    post_order_(tree)
    print()
    postorder_(tree)

    print()

