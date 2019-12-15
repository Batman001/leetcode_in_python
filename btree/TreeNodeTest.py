# -*- coding:utf-8- -*-
from btree.TreeNode import CreateTree


def pre_order(root):
    """
    递归前序遍历
    :param root: 二叉树的根节点
    :return:
    """
    if root is None:
        return
    print(root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)


def pre_order_2(root):
    stack = [root]

    while stack:
        cur_node = stack.pop()
        print(cur_node.val, end=" ")
        if cur_node.right is not None:
            stack.append(cur_node.right)
        if cur_node.left is not None:
            stack.append(cur_node.left)


def pre_order_(root):
    """
    非递归前序遍历
    (1)使用栈存储二叉树 初始化为根节点
    (2)在pop的时候访问当前节点
    (3)先添加右子树
    (4)再添加左子树
    :param root:
    :return:
    """
    if root is None:
        return
    stack = [root]
    while stack:
        cur_node = stack.pop()
        print(cur_node.val, end=" ")
        if cur_node.right is not None:
            stack.append(cur_node.right)
        if cur_node.left is not None:
            stack.append(cur_node.left)


def in_order(root):
    """
    递归中序遍历
    :param root: 二叉树根节点
    :return:
    """
    if root is None:
        return
    in_order(root.left)
    print(root.val, end=" ")
    in_order(root.right)


def in_order_2(root):
    stack = []
    while stack or root is not None:
        while root is not None:
            stack.append(root)
            root = root.left

        if stack:
            cur_node = stack.pop()
            print(cur_node.val, end=" ")
            root = cur_node.right


def in_order_(root):
    """
    中序非递归遍历
    (1)现将全部的左子树添加进栈中
    (2)pop元素 访问当前pop元素的右子树
    :param root:
    :return:
    """
    if root is None:
        return
    stack = []

    while stack or root is not None:
        while root is not None:
            stack.append(root)
            root = root.left
        if stack:
            cur_node = stack.pop()
            print(cur_node.val, end=" ")
            root = cur_node.right


def post_order(root):
    """
    递归后序遍历
    :param root: 二叉树的根节点
    :return:
    """
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=" ")


def post_order_2(root):
    stack = [root]
    reverse_stack = []

    while stack:
        cur_node = stack.pop()

        reverse_stack.append(cur_node)

        if cur_node.left is not None:
            stack.append(cur_node.left)

        if cur_node.right is not None:
            stack.append(cur_node.right)

    while reverse_stack:
        print(reverse_stack.pop().val, end=" ")


def post_order_(root):
    """
    非递归后序遍历
    :param root:
    :return:
    """
    if root is None:
        return
    stack = [root]
    reverse_stack = []
    while stack:
        cur_node = stack.pop()
        reverse_stack.append(cur_node)

        if cur_node.left is not None:
            stack.append(cur_node.left)

        if cur_node.right is not None:
            stack.append(cur_node.right)

    while reverse_stack:
        print(reverse_stack.pop().val, end=" ")


if __name__ == "__main__":
    array_string = " [3, 5, 1,6, 2,0, 8,null,null,7,4]"
    root = CreateTree.create_tree_by_string(array_string)
    print("前序遍历结果为:")
    pre_order(root)
    print()
    print("前序非递归遍历结果为:")
    pre_order_2(root)
    print()

    print("中序遍历的结果为:")
    in_order(root)
    print()

    print("中序非递归遍历的结果为:")
    in_order_2(root)
    print()

    print("后序遍历的结果为:")
    post_order(root)
    print()

    print("后序非遍历的结果为:")
    post_order_2(root)
    print()



