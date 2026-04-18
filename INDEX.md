# LeetCode Python 题目分类索引

## 目录结构

本项目按照算法类型进行分类，包含以下主要目录：

---

## 1. 数组相关 (array_relate/)
数组操作的各类题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [binary_search.py](array_relate/binary_search.py) | - | 二分查找实现 | 二分查找 |
| [searchMatrix.py](array_relate/searchMatrix.py) | 74 | 搜索二维矩阵 | 二分查找 |
| [leetcode287.py](array_relate/leetcode287.py) | 287 | 寻找重复数 | 快慢指针/排序 |
| [topk.py](array_relate/topk.py) | - | TopK问题 | 堆排序 |
| [FindUnsortedSubarrry.py](array_relate/FindUnsortedSubarrry.py) | 581 | 最短无序连续子数组 | 数组遍历 |
| [word_search.py](array_relate/word_search.py) | 79 | 单词搜索 | DFS/回溯 |
| [next_greate_element.py](array_relate/next_greate_element.py) | - | 下一个更大元素 | 单调栈 |
| [is_palindrome.py](array_relate/is_palindrome.py) | - | 回文判断 | 双指针 |

---

## 2. 滑动窗口 (sliding_window/)
滑动窗口算法相关题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [leetcode_3.py](sliding_window/leetcode_3.py) | 3 | 无重复字符的最长子串 | 滑动窗口 |
| [leetcode_76.py](sliding_window/leetcode_76.py) | 76 | 最小覆盖子串 | 滑动窗口 |
| [leetcode_209.py](sliding_window/leetcode_209.py) | 209 | 长度最小的子数组 | 滑动窗口 |
| [leetcode_239.py](sliding_window/leetcode_239.py) | 239 | 滑动窗口最大值 | 双端队列 |
| [leetcode_438.py](sliding_window/leetcode_438.py) | 438 | 找到字符串中所有字母异位词 | 滑动窗口 |
| [minWindow.py](sliding_window/minWindow.py) | 76 | 最小覆盖子串(另一实现) | 滑动窗口 |
| [min_subarray_len.py](sliding_window/min_subarray_len.py) | 209 | 最小子数组长度 | 滑动窗口 |

---

## 3. 动态规划 (dp/)
动态规划经典题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [bag.py](dp/bag.py) | - | 01背包问题 | 动态规划 |
| [edit-distance.py](dp/edit-distance.py) | 72 | 编辑距离 | 动态规划 |
| [longest-common-sub-sequence.py](dp/longest-common-sub-sequence.py) | - | 最长公共子序列(LCS) | 动态规划 |
| [longest-common-sub-string.py](dp/longest-common-sub-string.py) | - | 最长公共子串 | 动态规划 |
| [max_profit.py](dp/max_profit.py) | 121 | 买卖股票的最佳时机 | 动态规划 |
| [ClimbStair.py](dp/ClimbStair.py) | 70 | 爬楼梯 | 动态规划 |
| [CoinChange.py](dp/CoinChange.py) | 322 | 零钱兑换 | 动态规划 |

---

## 4. 二叉树 (btree/)
二叉树相关题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [LeetCodeSolution.py](btree/LeetCodeSolution.py) | 112, 129, 236, 101, 814, 543, 124, 617 | 多个二叉树题目 | 递归/DFS |
| [TreeNode.py](btree/TreeNode.py) | - | 二叉树节点定义 | 数据结构 |
| [TreeNodeFunction.py](btree/TreeNodeFunction.py) | - | 二叉树基本操作 | 递归 |
| [binary_tree.py](btree/binary_tree.py) | - | 二叉树基础 | 递归 |

**LeetCodeSolution.py 包含题目详情：**
- **112**: 路径总和 - 判断是否存在根到叶子节点路径和等于目标
- **129**: 求根到叶子节点数字之和
- **236**: 二叉树的最近公共祖先
- **101**: 判断二叉树是否镜像对称
- **814**: 二叉树剪枝 - 移除不包含1的子树
- **543**: 二叉树的直径
- **124**: 二叉树最大路径和
- **617**: 合并两个二叉树

---

## 5. 回溯算法 (backtracking/)
回溯法求解组合问题

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [Queen_Solution.py](backtracking/Queen_Solution.py) | 51, 52 | N皇后问题 | 回溯 |

---

## 6. 排序算法 (sort/)
各类排序算法实现

| 文件名 | 算法类型 | 描述 |
|--------|----------|------|
| [QuickSort.py](sort/QuickSort.py) | 快速排序 | 经典快排实现 |
| [MergeSort.py](sort/MergeSort.py) | 归并排序 | 归并排序实现 |
| [HeapSort.py](sort/HeapSort.py) | 堆排序 | 堆排序实现 |
| [MaxHeap.py](sort/MaxHeap.py) | 最大堆 | 最大堆数据结构 |
| [MinHeap.py](sort/MinHeap.py) | 最小堆 | 最小堆数据结构 |
| [TopK.py](sort/TopK.py) | TopK | 使用堆查找第K大元素 |
| [HashSort.py](sort/HashSort.py) | 哈希排序 | 基于哈希的排序 |

---

## 7. 链表相关 (linkedlist_relate/)
链表操作题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [ReverstListNode.py](linkedlist_relate/ReverstListNode.py) | 92 | 反转链表II | 双指针 |
| [ReverseKGroup.py](linkedlist_relate/ReverseKGroup.py) | 25 | K个一组翻转链表 | 递归 |

---

## 8. 字符串相关 (string_relate/)
字符串处理题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [minWindow.py](string_relate/minWindow.py) | 76 | 最小覆盖子串 | 滑动窗口 |
| [HashMapSort.py](string_relate/HashMapSort.py) | - | 哈希映射排序 | 哈希 |

---

## 9. KMP算法 (kmp/)
字符串匹配算法

| 文件名 | 描述 |
|--------|------|
| [kmp.py](kmp/kmp.py) | KMP算法实现 |
| [violent_match.py](kmp/violent_match.py) | 暴力匹配算法 |

---

## 10. 图遍历 (graph_traversal/)
图的遍历和搜索

| 文件名 | 描述 | 解法类型 |
|--------|------|----------|
| [GraphTraversal.py](graph_traversal/GraphTraversal.py) | BFS/DFS遍历 | 队列/栈 |
| [GraphReview.py](graph_traversal/GraphReview.py) | 图遍历复习 | BFS/DFS |
| [dijkstra.py](graph_traversal/dijkstra.py) | Dijkstra最短路径 | 最短路径算法 |

---

## 11. 排列组合 (permutation/)
排列组合问题

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [subsets.py](permutation/subsets.py) | 78 | 子集 | 回溯 |
| [PermTest.py](permutation/PermTest.py) | - | 排列测试 | 回溯 |
| [Solution.py](permutation/Solution.py) | - | 排列组合 | 回溯 |

---

## 12. 贪心算法 (greedy_algorithm/)
贪心算法题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [remove_k_digits.py](greedy_algorithm/remove_k_digits.py) | 402 | 移掉K位数字 | 贪心+栈 |

---

## 13. Trie树 (trie/)
前缀树数据结构

| 文件名 | LeetCode编号 | 题目描述 |
|--------|-------------|----------|
| [TrieTree.py](trie/TrieTree.py) | - | Trie树实现 |
| [trie_solution.py](trie/trie_solution.py) | - | Trie应用 |
| [ByteDanceTrie.py](trie/ByteDanceTrie.py) | - | 字节跳动Trie面试题 |

---

## 14. 矩阵相关 (matrix/)
矩阵操作题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [spiralOrder.py](matrix/spiralOrder.py) | 54, 59 | 螺旋矩阵 | 边界遍历 |

---

## 15. K Sum问题 (ksum/)
多元素求和问题

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [two-sum.py](ksum/two-sum.py) | 1 | 两数之和 | 哈希表 |

---

## 16. 其他题目 (other/)
其他类型题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [RomanToInteger.py](other/RomanToInteger.py) | 13 | 罗马数字转整数 | 哈希 |
| [leetcode-26.py](other/leetcode-26.py) | 26 | 删除有序数组中的重复项 | 双指针 |
| [NestedIterator.py](other/NestedIterator.py) | 341 | 扁平化嵌套列表迭代器 | 栈 |

---

## 17. 数学相关 (math/)
数学类题目

| 文件名 | LeetCode编号 | 题目描述 | 解法类型 |
|--------|-------------|----------|----------|
| [my_sqrt.py](math/my_sqrt.py) | 69 | x的平方根 | 二分查找 |

---

## 18. 搜索算法 (search/)
搜索算法实现

| 文件名 | 描述 |
|--------|------|
| [Binaryearch.py](search/Binaryearch.py) | 二分查找 |

---

## 需要整理的文件

以下文件需要合并或移动到相应分类：

| 当前位置 | 问题 | 建议处理 |
|----------|------|----------|
| `aa.py` (根目录) | 移掉K位数字贪心算法 | 移入 `greedy_algorithm/` |
| `review.py` (根目录) | TopK问题堆/快排实现 | 移入 `sort/` |
| `baidu_INTERVIEW.py` (根目录) | 快排+股票最大利润 | 分拆到 `sort/` 和 `dp/` |
| `linkedlist_relate/ReverstListNode.py` | 包含subsets和merge函数 | 分拆独立文件 |
| `sliding_window/minWindow.py` + `string_relate/minWindow.py` | 重复leetcode76 | 合并 |

---

## 统计

- **总题目数**: 约70+道
- **涵盖LeetCode编号**: 1, 3, 13, 25, 26, 51, 52, 54, 59, 69, 70, 72, 74, 76, 78, 79, 92, 101, 121, 124, 129, 209, 236, 239, 287, 322, 341, 402, 438, 543, 581, 617, 814, 124等

---

## 学习建议

1. **入门顺序**: 数组 → 排序 → 链表 → 二叉树 → 动态规划
2. **面试高频**: 滑动窗口、动态规划、二叉树、回溯
3. **重点题目**: 
   - 数组: 287, 74
   - 滑动窗口: 3, 76, 239
   - 动态规划: 72, 121, 322
   - 二叉树: 236, 124, 543
   - 回溯: 51, 78