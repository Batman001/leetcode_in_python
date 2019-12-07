# -*- coding:utf-8 -*-


class MinHeap:
    """
    小顶堆的类
    第一步：先n个元素的无序序列，构建成小顶堆 (父节点的元素值小于左右子节点的元素值)

    第二步：将根节点与最后一个元素交换位置，（将最小元素"沉"到数组末端）

    第三步：交换过后可能不再满足小顶堆的条件，所以需要将剩下的n-1个元素重新构建成小顶堆(调用调整堆方法 传入堆顶的索引位置0)

    第四步：重复第二步、第三步直到整个数组排序完成
    """
    def __init__(self, array):
        self.heap = array
        self.heap_size = len(array)

    def build_heap(self):
        """
        建立小根堆的方法
        从最后一个非叶子节点开始进行调整
        :return:
        """
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.adjust_heap(i)

    def adjust_heap(self, index):
        """
        调整索引为值为index的堆
        :param index: 索引位置
        :return:
        """
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2
        min_index = index
        if left_child_index < self.heap_size and \
                self.heap[left_child_index] < self.heap[index]:
            min_index = left_child_index

        if right_child_index < self.heap_size and \
                self.heap[right_child_index] < self.heap[min_index]:
            min_index = right_child_index

        # 如果当前调整的堆的索引位置不满足最小堆情形 则需要互换min_index与index位置的元素
        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self.adjust_heap(min_index)

    def heap_sort(self):
        """
        对建立好的最小堆进行排序, 即需要不断将堆顶元素(最小)与堆尾元素互换 然后动态调整堆顶 遍历n次

        :return:
        """
        for i in range(len(self.heap)):
            self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
            self.heap_size -= 1
            self.adjust_heap(0)


if __name__ == "__main__":
    nums = [1, -9, 45, -5, 89, 3, 0, 1.5, 9, 10]
    print("未建立堆之前的nums数组为:")
    print(nums)

    min_heap = MinHeap(nums)
    min_heap.build_heap()
    print("建立小根堆之后的nums数组为:")
    print(min_heap.heap)

    min_heap.heap_sort()
    print("经过小根堆排序后的nums数组为:")
    print(min_heap.heap)











