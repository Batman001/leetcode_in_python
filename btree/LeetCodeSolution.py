# -*- coding:utf-8 -*-
from btree import TreeNode
from btree.TreeNode import CreateTree


class LeetCodeSolution(object):

    def __init__(self, question_num, all_paths=[]):
        """
        初始化参数
        :param question_num: leetCode题目编号
        """
        self.question_num = question_num
        self.all_paths = all_paths

    def execute(self):
        print("当前leetcode题目号码是:" + str(self.question_num))
        print("执行的结果为:")

    def has_path_sum(self, root, sum_data):
        """
        路径总和 给定一个二叉树和一个目标和,判断该树中是否存在根节点到叶子节点的路径,这条路径上所有节点值相加等于目标和
        :param root: TreeNode
        :param sum_data: int 根节点到叶子节点路径的和
        :return: boolean
        """
        if root is None:
            return False
        sum_data -= root.val
        if sum_data == 0 and root.left is None and root.right is None:
            return True
        return self.has_path_sum(root.left, sum_data) or self.has_path_sum(root.right, sum_data)

    def sum_numbers(self, root):
        """
        leetcode129 求根到叶子节点数字之和
        :param root: TreeNode
        :return: int
        """
        res = self.find_all_path(root)
        res = [[str(_) for _ in item] for item in res]
        res = ["".join(item) for item in res]
        return sum([int(item) for item in res])

    def find_all_path(self, root):
        if root is None:
            return self.all_paths
        global one_path
        one_path.append(root.val)
        if root.left is None and root.right is None:
            # 使用一个临时容器将每一个完整的从根节点到叶子节点的的路径进行存储
            current_path = [item for item in one_path]
            self.all_paths.append(current_path)

        self.find_all_path(root.left)
        self.find_all_path(root.right)
        one_path.pop()
        return self.all_paths


if __name__ == "__main__":
    tree = TreeNode.InitTree().init_tree()
    lc1 = LeetCodeSolution(112)
    lc1.execute()
    print(lc1.has_path_sum(tree, 30))

    print("=====================================")

    one_path = []
    lc2 = LeetCodeSolution(129)
    lc2.execute()
    tree_ = CreateTree('49051').create_tree_by_list()
    print(lc2.sum_numbers(tree_))

