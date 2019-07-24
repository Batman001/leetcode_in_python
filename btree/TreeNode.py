# -*- coding:utf-8 -*-
from graphviz import Digraph
import random
import uuid


class TreeNode:
    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.dot = Digraph(comment='Binary Tree')

    def pre_order(self):
        """ 前序递归遍历 """
        if self.val is not None:
            print(self.val, end=" ")
        if self.left is not None:
            self.left.pre_order()
        if self.right is not None:
            self.right.pre_order()

    def pre_order_(self):
        """前序非递归遍历 使用栈结构实现"""
        res_ = []
        if self is None:
            return res_
        stack = [self]

        while stack:
            cur_node = stack.pop()
            # print(cur_node.val, end=" ")
            res_.append(cur_node.val)
            if cur_node.right is not None:
                stack.append(cur_node.right)

            if cur_node.left is not None:
                stack.append(cur_node.left)
        return res_

    def in_order(self):
        """ 中序递归遍历 """
        if self.left is not None:
            self.left.in_order()
        if self.val is not None:
            print(self.val, end=" ")
        if self.right is not None:
            self.right.in_order()

    def in_order_(self):
        """
        中序非递归遍历
        :return: 遍历的结果使用列表进行存储
        """
        res_ = []
        if self is None:
            return res
        # 使用外部栈结构对二叉树进行非递归中序遍历
        stack = []
        root = self
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            if stack:
                cur_node = stack.pop()
                res_.append(cur_node.val)
                root = cur_node.right
        return res_

    def post_order(self):
        """ 后序递归遍历 """
        if self.left is not None:
            self.left.post_order()
        if self.right is not None:
            self.right.post_order()
        if self.val is not None:
            print(self.val, end=" ")

    def post_order_(self):
        """
        后序非递归遍历
        :return: 后序非递归遍历的结果使用列表进行存储
        :solution 借助前序非递归遍历 使用 根 -> 右节点 -> 左节点 然后逆序输出非递归遍历结果
        """
        res_ = []
        if self is None:
            return res
        stack = [self]
        stack_reverse = []
        while stack:
            cur_node = stack.pop()
            stack_reverse.append(cur_node)

            if cur_node.left is not None:
                stack.append(cur_node.left)

            if cur_node.right is not None:
                stack.append(cur_node.right)
        while stack_reverse:
            res_.append(stack_reverse.pop().val)
        return res_

    def level_order(self):
        """ 层次非递归遍历(借助队列实现) """
        result = [self]
        while result:
            current_node = result[0]
            result.remove(current_node)
            print(current_node.val, end=" ")
            if current_node.left is not None:
                result.append(current_node.left)
            if current_node.right is not None:
                result.append(current_node.right)

    def level_order_(self):
        #返回某个节点的左子树
        def left_of_node(cur_node):
            return cur_node.left if cur_node.left is not None else None

        #返回某个节点的右子树
        def right_of_node(cur_node):
            return cur_node.right if cur_node.right is not None else None

        #层次遍历列表
        levels_list = []
        # 是否添加根节点中的数据
        if self.val is not None:
            levels_list.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            for _ in range(2, height + 1):
                current_level = []
                for node in levels_list[-1]:
                    if left_of_node(node):
                        current_level.append(left_of_node(node))
                    if right_of_node(node):
                        current_level.append(right_of_node(node))
                # 如果该层不为空 则添加该层
                if current_level:
                    levels_list.append(current_level)
            # 取出每层中的数据
            for i in range(0, height):
                for index in range(len(levels_list[i])):
                    levels_list[i][index] = levels_list[i][index].val
        return levels_list

    def level_order_list(self):
        """
        层次遍历非递归实现 并且返回按照层次输出层次遍历的结果lists
        leetcode102. 二叉树的层次遍历
        :return:
        """
        result = []
        if not self:
            return result
        level_nodes = [self]

        while level_nodes:
            next_level_nodes = []
            result.append([])
            for node in level_nodes:
                result[-1].append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            level_nodes = next_level_nodes
        return result

    def height(self):
        """ 返回二叉树的高度 """
        '''树的高度为0,只有root节点的高度为1'''
        if self.val is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    def leaves(self):
        """ 返回二叉树的叶子节点 """
        if self.val is None:
            return None
        elif self.left is None and self.right is None:
            print(self.val, end=" ")
        elif self.left is not None and self.right is None:
            self.left.leaves()
        elif self.left is None and self.right is not None:
            self.right.leaves()
        else:
            self.left.leaves()
            self.right.leaves()

    # 利用GraphViz实现二叉树的可视化
    def print_tree(self, save_path='./Binary_Tree.gv', label=False):

        # colors for labels of nodes
        colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']

        # 绘制以某个节点为根节点的二叉树
        def print_node(node, node_tag):
            # 节点颜色
            color = random.sample(colors, 1)[0]
            if node.left is not None:
                left_tag = str(uuid.uuid1())  # 左节点的数据
                self.dot.node(left_tag, str(node.left.val), style='filled', color=color)  # 左节点
                label_string = 'L' if label else ''  # 是否在连接线上写上标签，表明为左子树
                self.dot.edge(node_tag, left_tag, label=label_string)  # 左节点与其父节点的连线
                print_node(node.left, left_tag)

            if node.right is not None:
                right_tag = str(uuid.uuid1())
                self.dot.node(right_tag, str(node.right.val), style='filled', color=color)
                label_string = 'R' if label else ''  # 是否在连接线上写上标签，表明为右子树
                self.dot.edge(node_tag, right_tag, label=label_string)
                print_node(node.right, right_tag)

        # 如果树非空
        if self.val is not None:
            root_tag = str(uuid.uuid1())  # 根节点标签
            self.dot.node(root_tag, str(self.val), style='filled', color=random.sample(colors, 1)[0])  # 创建根节点
            print_node(self, root_tag)

        self.dot.render(save_path)


class InitTree:
    def __init__(self):
        pass

    @staticmethod
    def init_tree():
        # 构造二叉树, BOTTOM-UP METHOD
        right_tree = TreeNode(6)

        right_tree.left = TreeNode(2)
        right_tree.right = TreeNode(4)

        left_tree = TreeNode(5)
        left_tree.left = TreeNode(1)
        left_tree.right = TreeNode(3)

        con_tree = TreeNode(11)
        con_tree.left = left_tree
        con_tree.right = right_tree

        left_tree = TreeNode(7)
        left_tree.left = TreeNode(3)
        left_tree.right = TreeNode(4)

        right_tree = con_tree  # 增加新的变量
        con_tree = TreeNode(18)
        con_tree.left = left_tree
        con_tree.right = right_tree
        return con_tree


class CreateTree(object):

    def __init__(self, arr):
        self.array = arr

    """ 利用列表构造二叉树 列表中至少有一个元素 """
    def create_tree_by_list(self):
        i = 1
        # 将原数组拆成层次遍历的数组，每一项都储存这一层所有的节点的数据
        level_order = []
        sum_data = 1

        while sum_data < len(self.array):
            level_order.append(self.array[i-1:2*i-1])
            i *= 2
            sum_data += i
        level_order.append(self.array[i-1:])
        print(level_order)

        def create_tree_one_step_up(tree_lists, forward_level):
            """
            按步骤进行树的创建
            :param tree_lists: 这一层所有节点组成的列表
            :param forward_level: 上一层节点的数据组成的列表
            :return:
            """
            new_tree_list = []
            index_ = 0
            for elem in forward_level:
                root = TreeNode(elem)
                if 2 * index_ < len(tree_lists):
                    root.left = tree_lists[index_ * 2]
                if 2 * index_ + 1 < len(tree_lists):
                    root.right = tree_lists[index_ * 2 + 1]
                new_tree_list.append(root)
                index_ += 1
            return new_tree_list

        # 如果只有一个节点
        if len(level_order) == 1:
            return TreeNode(level_order[0][0])
        # 二叉树的层数大于1
        else:

            # 创建最后一层的节点列表
            tree_list = [TreeNode(elem) for elem in level_order[-1]]

            # 从下往上,逐层构建二叉树
            for i in range(len(level_order)-2, -1, -1):
                tree_list = create_tree_one_step_up(tree_list, level_order[i])

            return tree_list[0]


if __name__ == "__main__":
    tree = InitTree().init_tree()
    print("层序遍历为:")
    print(tree.level_order())

    print("\n")
    print("层次递归遍历为:")
    print(tree.level_order_())

    print("二叉树的叶子节点为:")
    tree.leaves()
    print("\n")

    print("二叉树的高度为:" + str(tree.height()))

    tree.print_tree(save_path='/Users/sunchao/Desktop/tree.gv', label=True)

    array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    array1 = '49051'
    tree_ = CreateTree(array1).create_tree_by_list()
    tree_.print_tree(save_path='/Users/sunchao/Desktop/tree_.gv', label=True)

    print("二叉树前序递归遍历:")
    tree.pre_order()
    print()

    print("二叉树前序非递归遍历:")
    res = tree.pre_order_()
    print(res)
    print()

    print("二叉树中序递归遍历:")
    tree.in_order()
    print()

    print("二叉树中序非递归遍历:")
    res = tree.in_order_()
    print(res)
    print()

    print("二叉树后序递归遍历:")
    tree.post_order()
    print()

    print("二叉树后序非递归遍历:")
    res = tree.post_order_()
    print(res)
    print()

    print("二叉树层次遍历的:")
    print(tree.level_order_list())
    print(tree.level_order())
    print(tree.level_order_())








