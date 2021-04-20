# -*- coding:utf-8 -*-


class MaxHeap:
    """
        大顶堆的类
        第一步：先n个元素的无序序列，构建成大顶堆 (父节点的元素值大于左右子节点的元素值)

        第二步：将根节点与最后一个元素交换位置，（将最大元素"沉"到数组末端）

        第三步：交换过后可能不再满足大顶堆的条件，所以需要将剩下的n-1个元素重新构建成大顶堆(调用调整堆方法 传入堆顶的索引位置0)

        第四步：重复第二步、第三步直到整个数组排序完成
        """
    def __init__(self, array):
        self.heap = array
        self.heap_size = len(array)

    def build_heap(self):
        """
        建堆过程函数
        :return:
        """
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.adjust_heap(i)

    def adjust_heap(self, index):
        """
        动态调整索引位置为index的元素使其成为大顶堆
        :param index: 索引位置
        :return:
        """
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        max_index = index
        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            max_index = left_index
        if right_index < self.heap_size and self.heap[right_index] > self.heap[max_index]:
            max_index = right_index

        if max_index != index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self.adjust_heap(max_index)

    def heap_sort(self):
        """
        不断将堆顶元素与堆尾元素互换(使堆顶最大元素沉底) 然后动态调整n-1的剩余元素 使其成为大顶堆
        :return:
        """
        for i in range(self.heap_size):
            self.heap[0], self.heap[self.heap_size -1] = self.heap[self.heap_size - 1], self.heap[0]
            self.heap_size -= 1
            self.adjust_heap(0)


if __name__ == "__main__":
    nums = [1, -9, 45, -5, 89, 3, 0, 1.5, 9, 10]
    nums = [1, 3, 2, 48, 70, 18, 999, 101, 124, 216]
    print("未建立堆之前的nums数组为:")
    print(nums)

    max_heap = MaxHeap(nums)
    max_heap.build_heap()
    print("建立大根堆之后的nums数组为:")
    print(max_heap.heap)

    max_heap.heap_sort()
    print("经过大根堆排序后的nums数组为:")
    print(max_heap.heap)
