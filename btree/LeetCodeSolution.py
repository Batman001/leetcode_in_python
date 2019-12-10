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

    def lowest_common_ancestor(self, root, p, q):
        """
        leetcode 二叉树的最近公共祖先(递归实现)
        :param root 二叉树的根节点
        :param p: 二叉树某一节点p
        :param q: 二叉树某一节点q
        :return: TreeNode 最近祖先节点
        """
        if root is None or root == p or root == q:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)

        right = self.lowest_common_ancestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        return left if right is None else right

    def get_path(self, root, node, path):
        """
        得到从root根节点到 node 节点的路径信息 不断更新path中列表 path中存储的即为路径信息
        :param root 二叉树根节点
        :param node: 二叉树某一个节点
        :param path: 路径信息存储列表
        :return:
        """
        if not root or not node:
            return False
        if root == node:
            return True

        path.append(root)

        found = False

        if root.left is not None:
            found = self.get_path(root.left, node, path)

        if not found and root.right is not None:
            found = self.get_path(root.right, node, path)

        if not found:
            path.pop()
        return found

    def lowest_common_ancestor_(self, root, p, q):
        """
        leetcode236 二叉树的最近公共祖先(非递归实现)
        :param root: 根节点
        :param p: 二叉树某一节点p
        :param q: 二叉树某一节点q
        :return: TreeNode 最近祖先节点
        """
        path = []
        self.get_path(root, p, path)
        path.append(p)

        path_ = []
        self.get_path(root, q, path_)
        path_.append(q)

        # 然后根据路径1和路径2, 从后向前寻找出现的最先公共节点
        for i in range(len(path)-1, -1, -1):
            if path[i] in path_:
                return path[i]
        return None

    def is_symmetric(self, root):
        """
        leetcode101 判断一个二叉树是不是一个镜像对称的二叉树(递归实现)
        :param root: 二叉树根节点
        :return: boolean 是否为镜像二叉树
        """
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left, right):
        """
        判断两个二叉树的左右子树是否为镜像二叉树
        :param left: 左子树
        :param right: 右子树
        :return: boolean
        """
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)

    @staticmethod
    def is_symmetric_(root):
        """
        leetcode101 判断一个二叉树是不是一个镜像对称的二叉树(非递归实现)
        解决方法:层次遍历 判断每一层是不是回文数组
        :param root: 二叉树根节点
        :return: boolean True or False
        """
        queue = [root]
        while queue:
            next_queue = list()
            layer = list()
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)

                layer.append(node.val)

            # 判断每一层的val是否为回文字符串
            if layer != layer[::-1]:
                return False

            queue = next_queue
        return True

    def prune_tree(self, root):
        """
        leetcode 814 二叉树的剪枝 (使用递归实现）
        给定二叉树根结点 root，此外树的每个结点的值要么是 0，要么是 1。
        返回移除了所有不包含 1 的子树的原二叉树。
        :param root: 待剪枝的二叉树的根节点
        :return: 剪枝后的二叉树根节点
        """
        if root is None:
            return None
        root.left = self.prune_tree(root.left)
        root.right = self.prune_tree(root.right)

        if root.left is None and root.right is None and root.val == 0:
            return None

        return root


def merge_tree(t1, t2):
    """
    LeetCode617,合并两个二叉树 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
    你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
    否则不为 NULL 的节点将直接作为新二叉树的节点。
    :param t1: 二叉树t1
    :param t2: 二叉树t2
    :return: 返回新的合并后的二叉树
    """
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    new_root = TreeNode()
    new_root.val = t1.val + t2.val
    new_root.left = merge_tree(t1.left, t2.left)
    new_root.right = merge_tree(t1.right, t2.right)
    return new_root


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

    print("=====================================")
    lc3 = LeetCodeSolution(236)
    lc3.execute()

    ancestor = lc3.lowest_common_ancestor(tree, tree.right.left.left, tree.right.right)
    ancestor_ = lc3.lowest_common_ancestor_(tree, tree.right.left.left, tree.right.right)
    print(ancestor.val)
    print(ancestor_.val)
