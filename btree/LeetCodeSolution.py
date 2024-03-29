# -*- coding:utf-8 -*-
from btree import TreeNode
from btree.TreeNode import CreateTree


class LeetcodeSolution(object):

    def __init__(self, question_num, all_paths=None):
        """
        初始化参数
        :param question_num: leetcode题目编号
        """
        # 设置二叉树最大直径的全局变量，仅供leetcode543使用
        self.max_len = 0

        # 设置二叉树的全部节点的计算的最大值，仅供leetcode124使用；切记不为0！！！！，否则对于只有一个根节点，且为负值的例子，不通过！！！！
        self.max_val = float('-inf')

        if all_paths is None:
            all_paths = []
        self.question_num = question_num
        self.all_paths = all_paths

    def execute(self):
        print("=====================================")
        print("当前leetcode题目号码是:" + str(self.question_num))
        print("执行的结果为:")

    def has_path_sum(self, root, sum_data):
        """
        leetcode 112 路径总和
        https://leetcode-cn.com/problems/path-sum/
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
        https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
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
        leetcode236 二叉树的最近公共祖先(递归实现)
        https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
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
        https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
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
        https://leetcode-cn.com/problems/symmetric-tree/
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
        https://leetcode-cn.com/problems/symmetric-tree/
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
        https://leetcode-cn.com/problems/binary-tree-pruning/
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

    def diameterOfBinaryTree(self, root):
        """
        leetcode 543 https://leetcode-cn.com/problems/diameter-of-binary-tree/
        给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
        这条路径可能穿过根结点。
        :type root: 二叉树根节点
        :rtype: int 返回最长直径
        """
        self.depth(root)
        return self.max_len

    def depth(self, root):
        """
        1）step1：递归求解左右子树高度，返回根节点最大的高度
        2）step2：在执行过程中不断更新max_len
        :param root:
        :return:
        """
        if root is None:
            return 0

        left_height = self.depth(root.left)
        right_hight = self.depth(root.right)
        self.max_len = max(self.max_len, left_height + right_hight)
        return max(left_height, right_hight) + 1

    def diameterOfBinaryTree(self, root):
        """
        leetcode 124 https://leetcode.cn/problems/binary-tree-maximum-path-sum/
        二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。
        该路径 至少包含一个节点，且不一定经过根节点。路径和 是路径中各节点值的总和。
        :param root:
        :return:
        """
        self.depth_val(root)
        return self.max_val

    def depth_val(self, root):
        if root is None:
            return 0

        # 这里需要比较0和左节点的val的值，用于判断需不需要加这个孩子节点的值，作为增加值
        left_val = max(0, self.depth_val(root.left))
        right_val = max(0, self.depth_val(root.right))

        self.max_val = max(self.max_val, left_val+right_val+root.val)

        return max(left_val, right_val) + root.val


def merge_tree(t1, t2):
    """
    leetcode617,合并两个二叉树 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
    https://leetcode-cn.com/problems/merge-two-binary-trees/
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
    new_root = TreeNode
    new_root.val = t1.val + t2.val
    new_root.left = merge_tree(t1.left, t2.left)
    new_root.right = merge_tree(t1.right, t2.right)
    return new_root


def sumNumers(root):
    """
    leetcode129:求根节点到叶节点数字之和
    https://leetcode.cn/problems/sum-root-to-leaf-numbers/
    :param root:
    :return:
    """
    return helper(root, 0)


def helper(root, sum):
    """
    计算sumNumber的帮助函数，主要通过该函数进行递归,计算左右节点的和
    :param root: 根节点
    :param sum: 目前的累积的和
    :return:
    """
    if not root:
        return 0

    sum *= 10
    sum += root.val

    if not root.left and not root.right:
        return sum

    return helper(root.left, sum) + helper(root.right, sum)


def invertTree(root):
    if not root:
        return root

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root


if __name__ == "__main__":
    tree = TreeNode.InitTree().init_tree()
    lc1 = LeetcodeSolution(112)
    lc1.execute()
    print(lc1.has_path_sum(tree, 30))


    one_path = []
    lc2 = LeetcodeSolution(129)
    lc2.execute()
    tree_ = CreateTree('49051').create_tree_by_list()
    print(lc2.sum_numbers(tree_))

    lc3 = LeetcodeSolution(236)
    lc3.execute()

    ancestor = lc3.lowest_common_ancestor(tree, tree.right.left.left, tree.right.right)
    ancestor_ = lc3.lowest_common_ancestor_(tree, tree.right.left.left, tree.right.right)
    print(ancestor.val)
    print(ancestor_.val)


    lc4 = LeetcodeSolution(543)
    lc4.execute()
    print("二叉树的最大直径为:" + str(lc4.diameterOfBinaryTree(tree)))
