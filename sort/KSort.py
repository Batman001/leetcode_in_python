# -*- coding:utf-8 -*-
import sys
from typing import List, Optional


def left_index(root_index):
    """
    返回根节点为root_index的左子树的index
    :param root_index: 根节点的index
    :return: 右子树的index
    """
    return 2 * root_index + 1


def right_index(root_index):
    """
    返回根节点为root_index的右子树的index
    :param root_index: 根节点的index
    :return: 右子树的index
    """
    return 2 * root_index + 2


class HeapSort:
    def __init__(self, nums):
        self.nums = nums

    def build_heap(self, nums):
        """
        使用数组nums 建堆过程
        :param nums: 建堆数组
        :return:
        """
        nums_size = len(nums)
        for i in range(nums_size//2 - 1, -1, -1):
            self.max_modify(nums, i)

    def max_modify(self, heap, index):
        """
        动态调整heap中索引为index的堆
        结束条件： 如果largest等于index说明index是最大元素 或者 largest超出heap范围 说明不存在比i节点大的孩子节点
        调整完当前根节点之后，递归调用max_modify方法
        :param heap: 堆
        :param index: 索引
        :return: 调整后的heap
        """
        heap_size = len(heap)
        left = left_index(index)
        right = right_index(index)

        if left < heap_size and heap[left] > heap[index]:
            cur_largest = left
        else:
            cur_largest = index

        if right < heap_size and heap[right] > heap[cur_largest]:
            cur_largest = right

        if cur_largest == index or cur_largest >= heap_size:
            return

        # 交换heap[index]和heap[cur_largest]的值
        heap[index], heap[cur_largest] = heap[cur_largest], heap[index]
        self.max_modify(heap, cur_largest)

    def heap_sort(self, heap):
        """
        建堆并且动态调整完堆以后 进行排序(排序操作分为以下步骤)
        步骤一: 每次将堆顶元素与堆尾元素交换
        步骤二: heap.pop() 使用result接收堆尾元素
        步骤三: 使用max_modify 对堆顶元素进行堆调整
        :param heap: 堆
        :return: 排序后的result列表
        """
        result = []
        for i in range(len(heap)):
            heap_size = len(heap)
            heap[0], heap[heap_size - 1] = heap[heap_size - 1], heap[0]
            # 使用result 接收下沉到堆尾的大元素
            result.append(heap.pop())
            # 继续调整去除heap中大元素的其他剩余元素
            self.max_modify(heap, 0)
        return result

    def call(self):
        self.build_heap(self.nums)
        return self.heap_sort(self.nums)[::-1]


class MergeSort:
    """
    合并K个已排序数组
    """
    def merge_sort(self, nums):
        """
        已排序的多维数组 进行归并排序
        :param nums: 多维数组
        :return:
        """
        if(len(nums)) <= 1:
            return nums
        mid = len(nums) // 2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.sort_list(left, right)

    @staticmethod
    def sort_list(left, right):
        """
        对两个排好序的数组进行排序
        :param left: 排好序数组left
        :param right: 排好序数组right
        :return:
        """
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


Matrix = List[List[int]]


class MinHeapNode:
    def __init__(self, el, i, j):
        """
        :param el: the element to be sorted
        :param i: index of array from which element is taken
        :param j: index of next element to be picked from array
        """
        self.element = el
        self.i = i
        self.j = j


class MinHeap:
    """
    对列表建立小根堆 并进行堆排序
    """
    def __init__(self, ar: List[MinHeapNode], size: int):
        self.heap_size = size
        self.heap_arr = ar
        i = (self.heap_size - 1) // 2

        # 建立小根堆的过程
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def min_heapify(self, i):
        """
        小根堆调整过程
        :param i: 调整小根堆的对应列表的索引位置
        :return:
        """
        left = left_index(i)
        right = right_index(i)
        smallest = i

        if left < self.heap_size and self.heap_arr[left].element < self.heap_arr[i].element:
            smallest = left

        if right < self.heap_size and self.heap_arr[right].element < self.heap_arr[smallest].element:
            smallest = right

        if smallest != i:
            swap(self.heap_arr, i, smallest)
            self.min_heapify(smallest)

    def get_min(self) -> Optional:
        if self.heap_size <= 0:
            print("heap underflow")
            return None
        return self.heap_arr[0]

    def replace_min(self, root):
        self.heap_arr[0] = root
        self.min_heapify(0)


def swap(array: List[MinHeapNode], i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def merge_k_sorted_arrays(arr: Matrix, k: int):
    """

    :param arr: 已经排好序的k个有序列表的矩阵
    :param k: 矩阵中有序列表的数量
    :return: 返回归并排好序的结果
    """
    h_arr = []
    result_size = 0
    for i in range(len(arr)):
        node = MinHeapNode(arr[i][0], i, 1)
        h_arr.append(node)
        result_size += len(arr[i])

    min_heap = MinHeap(h_arr, k)
    result = [0] * result_size
    for i in range(result_size):
        root = min_heap.get_min()
        result[i] = root.element
        if root.j < len(arr[root.i]):
            root.element = arr[root.i][root.j]
            root.j += 1
        else:
            root.element = sys.maxsize
        min_heap.replace_min(root)

    for x in result:
        print(x, end=' ')
    print()


if __name__ == "__main__":
    sort = HeapSort([1, 3, 78, 34, 10, 9, 2, 5, -8])
    res = sort.call()
    print(res)

    merge_ = MergeSort()
    b = merge_.merge_sort([1, 3, 78, 34, 10, 9, 2, 5, -8])
    print(b)

    arr = [
        [2, 6, 12, 34],
        [1, 9, 20, 1000],
        [23, 34, 90, 2000]
    ]
    print('Merged Array is:')
    merge_k_sorted_arrays(arr, len(arr))


