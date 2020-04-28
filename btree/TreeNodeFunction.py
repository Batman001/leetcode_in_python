# -*- coding:utf-8 -*-
from btree.TreeNode import CreateTree


class TreeNodeFunction:
    """
    有关二叉树相关方法的类
    """

    def pre_order(self, root):
        """
        递归前序遍历
        :param root: 二叉树的根节点
        :return:
        """
        if not root:
            return
        print(root.val, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    @staticmethod
    def pre_order_(root):
        """
        非递归前序遍历
        (1)使用栈存储二叉树 初始化为根节点
        (2)在pop的时候访问当前节点
        (3)先添加右子树
        (4)再添加左子树
        :param root:二叉树根节点
        :return:
        """
        stack = [root]
        while stack:
            root = stack.pop()
            print(root.val, end=" ")
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

    def in_order(self, root):
        """
        二叉树递归中序遍历
        :param root:
        :return:
        """
        if not root:
            return
        self.in_order(root.left)
        print(root.val, end=" ")
        self.in_order(root.right)

    @staticmethod
    def in_order_(root):
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                cur_node = stack.pop()
                print(cur_node.val, end=" ")
                root = cur_node.right

    def post_order(self, root):
        """
        二叉树的后序费递归遍历
        :param root:
        :return:
        """
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val, end=" ")

    @staticmethod
    def post_order_(root):
        """
        二叉树的非递归后序遍历
        :param root:
        :return:
        """
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
            print(cur_node.val, end=" ")

    def get_height(self, root):
        """
        返回二叉树的高度(递归)
        :param root:
        :return:
        """
        if not root:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return max(left, right) + 1

    @staticmethod
    def get_height_(root):
        """
        二叉树的广度搜索 返回最大层数 即为二叉树的高度
        使用队列实现二叉树广度搜索
        :param root:
        :return:
        """
        if not root:
            return 0
        queue = [root]
        height = 0
        while queue:
            height += 1
            # 每一层递归时 进行高度+1操作
            for i in range(len(queue)):
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return height


if __name__ == "__main__":
    array_string = " [3, 5, 1,6, 2,0, 8,null,null,7,4]"
    tree = CreateTree.create_tree_by_string(array_string)
    func = TreeNodeFunction()
    print("前序遍历结果为:")
    func.pre_order(tree)
    print()
    print("前序非递归遍历结果为:")
    func.pre_order_(tree)
    print()

    print("中序遍历的结果为:")
    func.in_order(tree)
    print()

    print("中序非递归遍历的结果为:")
    func.in_order_(tree)
    print()

    print("后序遍历的结果为:")
    func.post_order(tree)
    print()

    print("后序非遍历的结果为:")
    func.post_order_(tree)
    print()

    print("二叉树递归计算的高度为：", str(func.get_height(tree)))

    print("二叉树非递归计算的高度为：", str(func.get_height_(tree)))
