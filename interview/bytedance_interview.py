# -*- coding:utf-8 -*-
"""
字节跳动面试高频LeetCode题目及解法

包含10道字节跳动面试中最常考的LeetCode题目:
1. LeetCode 1 - Two Sum (两数之和)
2. LeetCode 3 - Longest Substring Without Repeating Characters (无重复字符的最长子串)
3. LeetCode 15 - 3Sum (三数之和)
4. LeetCode 102 - Binary Tree Level Order Traversal (二叉树层序遍历)
5. LeetCode 121 - Best Time to Buy and Sell Stock (买卖股票的最佳时机)
6. LeetCode 146 - LRU Cache (LRU缓存机制)
7. LeetCode 200 - Number of Islands (岛屿数量)
8. LeetCode 206 - Reverse Linked List (反转链表)
9. LeetCode 215 - Kth Largest Element in an Array (数组中的第K个最大元素)
10. LeetCode 25 - Reverse Nodes in k-Group (K个一组翻转链表)
"""


# ==================== LeetCode 1 - Two Sum ====================
def two_sum(nums, target):
    """
    两数之和 - 使用哈希表，时间复杂度O(n)
    :param nums: 整数数组
    :param target: 目标和
    :return: 两个数的索引
    """
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []


# ==================== LeetCode 3 - Longest Substring Without Repeating Characters ====================
def length_of_longest_substring(s):
    """
    无重复字符的最长子串 - 滑动窗口
    :param s: 字符串
    :return: 最长子串长度
    """
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# ==================== LeetCode 15 - 3Sum ====================
def three_sum(nums):
    """
    三数之和 - 排序 + 双指针，时间复杂度O(n^2)
    :param nums: 整数数组
    :return: 所有和为0的三元组
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ==================== LeetCode 102 - Binary Tree Level Order Traversal ====================
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """
    二叉树层序遍历 - BFS
    :param root: 根节点
    :return: 层序遍历结果
    """
    if not root:
        return []

    from collections import deque
    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


# ==================== LeetCode 121 - Best Time to Buy and Sell Stock ====================
def max_profit(prices):
    """
    买卖股票的最佳时机 - 一次遍历
    :param prices: 股票价格数组
    :return: 最大利润
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


# ==================== LeetCode 146 - LRU Cache ====================
class LRUCache:
    """
    LRU缓存机制 - 哈希表 + 双向链表
    get和put操作时间复杂度均为O(1)
    """
    class DLinkedNode:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = self.DLinkedNode()
        self.tail = self.DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """将节点添加到链表头部"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """移除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        """将节点移动到头部"""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """移除尾部节点（最久未使用）"""
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            new_node = self.DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            node.value = value
            self._move_to_head(node)


# ==================== LeetCode 200 - Number of Islands ====================
def num_islands(grid):
    """
    岛屿数量 - DFS
    :param grid: 二维字符数组
    :return: 岛屿数量
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # 标记为已访问
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count


# ==================== LeetCode 206 - Reverse Linked List ====================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """
    反转链表 - 迭代法
    :param head: 链表头节点
    :return: 反转后的头节点
    """
    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    return prev


def reverse_list_recursive(head):
    """
    反转链表 - 递归法
    :param head: 链表头节点
    :return: 反转后的头节点
    """
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head


# ==================== LeetCode 215 - Kth Largest Element in an Array ====================
def find_kth_largest(nums, k):
    """
    数组中的第K个最大元素 - 小顶堆
    :param nums: 整数数组
    :param k: 第k大
    :return: 第k大的元素
    """
    import heapq

    # 使用大小为k的小顶堆
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


def find_kth_largest_quick_select(nums, k):
    """
    数组中的第K个最大元素 - 快速选择算法
    时间复杂度平均O(n)，最坏O(n^2)
    """
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] > pivot:  # 降序排列找第k大
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def quick_select(left, right, k_smallest):
        if left == right:
            return nums[left]

        pivot_index = partition(left, right, right)

        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quick_select(left, pivot_index - 1, k_smallest)
        else:
            return quick_select(pivot_index + 1, right, k_smallest)

    return quick_select(0, len(nums) - 1, k - 1)


# ==================== LeetCode 25 - Reverse Nodes in k-Group ====================
def reverse_k_group(head, k):
    """
    K个一组翻转链表
    :param head: 链表头节点
    :param k: 每组节点数
    :return: 翻转后的链表头节点
    """
    def reverse(head, tail):
        """翻转head到tail之间的节点"""
        prev = None
        curr = head
        while curr != tail:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    # 计算链表长度
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while length >= k:
        # 找到当前组的末尾
        tail = curr
        for _ in range(k - 1):
            tail = tail.next

        next_head = tail.next
        # 翻转当前组
        reverse(curr, tail.next)

        # 连接翻转后的链表
        prev.next = tail
        curr.next = next_head

        # 移动到下一组
        prev = curr
        curr = next_head
        length -= k

    return dummy.next


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 测试 Two Sum
    print("=== Two Sum ===")
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

    # 测试 Longest Substring Without Repeating Characters
    print("\n=== Longest Substring Without Repeating Characters ===")
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3

    # 测试 3Sum
    print("\n=== 3Sum ===")
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]

    # 测试 Max Profit
    print("\n=== Best Time to Buy and Sell Stock ===")
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5

    # 测试 Number of Islands
    print("\n=== Number of Islands ===")
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    print(num_islands(grid))  # 3

    # 测试 Find Kth Largest
    print("\n=== Kth Largest Element ===")
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(find_kth_largest_quick_select([3, 2, 1, 5, 6, 4], 2))  # 5

    # 测试 Reverse Linked List
    print("\n=== Reverse Linked List ===")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head = reverse_list(head)
    result = []
    while reversed_head:
        result.append(reversed_head.val)
        reversed_head = reversed_head.next
    print(result)  # [5, 4, 3, 2, 1]

    # 测试 LRU Cache
    print("\n=== LRU Cache ===")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # 1
    cache.put(3, 3)      # 淘汰 key=2
    print(cache.get(2))  # -1

    # 测试 Binary Tree Level Order Traversal
    print("\n=== Binary Tree Level Order Traversal ===")
    root = TreeNode(3,
                   TreeNode(9),
                   TreeNode(20, TreeNode(15), TreeNode(7)))
    print(level_order(root))  # [[3], [9, 20], [15, 7]]

    # 测试 Reverse K Group
    print("\n=== Reverse Nodes in k-Group ===")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = reverse_k_group(head, 2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output)  # [2, 1, 4, 3, 5]