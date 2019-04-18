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
            print(self.val,end=" ")
        if self.left is not None:
            self.left.pre_order()
        if self.right is not None:
            self.right.pre_order()

    def in_order(self):
        """ 中序递归遍历 """
        if self.left is not None:
            self.left.in_order()
        if self.val is not None:
            print(self.val, end=" ")
        if self.right is not None:
            self.right.in_order()

    def post_order(self):
        """ 后序递归遍历 """
        if self.left is not None:
            self.left.post_order()
        if self.right is not None:
            self.right.post_order()
        if self.val is not None:
            print(self.val, end=" ")

    def level_order(self):
        """ 层次非递归遍历(借助队列实现) """
        result = []
        result.append(self)
        while result != []:
            current_node = result[0]
            result.remove(current_node)
            print(current_node.val, end=" ")
            if current_node.left is not None:
                result.append(current_node.left)
            if current_node.right is not None:
                result.append(current_node.right)

    def level_order_(self):
        #返回某个节点的左子树
        def left_of_node(node):
            return node.left if node.left is not None else None

        #返回某个节点的右子树
        def right_of_node(node):
            return node.right if node.right is not None else None

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

    def init_tree(self):
        # 构造二叉树, BOTTOM-UP METHOD
        right_tree = TreeNode(6)
        a = TreeNode

        right_tree.left = TreeNode(2)
        right_tree.right = TreeNode(4)

        left_tree = TreeNode(5)
        left_tree.left = TreeNode(1)
        left_tree.right = TreeNode(3)

        tree = TreeNode(11)
        tree.left = left_tree
        tree.right = right_tree

        left_tree = TreeNode(7)
        left_tree.left = TreeNode(3)
        left_tree.right = TreeNode(4)

        right_tree = tree  # 增加新的变量
        tree = TreeNode(18)
        tree.left = left_tree
        tree.right = right_tree
        return tree


class CreateTree(object):

    def __init__(self, array):
        self.array = array

    """ 利用列表构造二叉树 列表中至少有一个元素 """
    def create_tree_by_list(self):
        i = 1
        # 将原数组拆成层次遍历的数组，每一项都储存这一层所有的节点的数据
        level_order = []
        sum = 1

        while sum < len(self.array):
            level_order.append(self.array[i-1:2*i-1])
            i *= 2
            sum += i
        level_order.append(self.array[i-1:])
        print(level_order)

        def create_tree_one_step_up(tree_list, forward_level):
            """
            按步骤进行树的创建
            :param tree_list: 这一层所有节点组成的列表
            :param forward_level: 上一层节点的数据组成的列表
            :return:
            """
            new_tree_list = []
            i = 0
            for elem in forward_level:
                root = TreeNode(elem)
                if 2 * i < len(tree_list):
                    root.left = tree_list[i*2]
                if 2 * i + 1 < len(tree_list):
                    root.right = tree_list[i*2+1]
                new_tree_list.append(root)
                i += 1
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





