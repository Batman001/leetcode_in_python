

def findKthNumWithHeap(nums, k):
    """
    通过堆排的思想的获取数组中第K大的元素，时间复杂度o(nlogk)
    :param nums:
    :param k:
    :return:
    """
    select_nums = nums[:k]
    b_heap = build_min_heap(select_nums)
    for i in range(k, len(nums)):
        if nums[i] > b_heap[0]:
            b_heap[0] = nums[i]
            adjust_min_heap(b_heap, 0)

    return heap_sort(b_heap)[0]


def build_min_heap(nums):
    """
    建立小根堆，即父节点的值要低于两个子节点的值
    :param nums:
    :return:
    """
    last_root_index = len(nums) // 2 - 1
    for i in range(last_root_index, -1, -1):
        adjust_min_heap(nums, i)
    return nums


def adjust_min_heap(heap, index):
    """
    动态调整堆的第index索引
    :param heap:
    :param index:
    :return:
    """
    left_index = index * 2 + 1
    right_index = index * 2 + 2
    length = len(heap)
    min_index = index

    if left_index < length and heap[left_index] < heap[index]:
        min_index = left_index

    if right_index < length and heap[right_index] < heap[min_index]:
        min_index = right_index

    if min_index != index:
        heap[index], heap[min_index] = heap[min_index], heap[index]
        adjust_min_heap(heap, min_index)


def heap_sort(heap):
    """
    对建好的堆进行排序，交换堆尾元素和堆顶元素后，通过res不断添加堆尾元素，然后动态调整堆顶元素
    复杂度o(klogk)
    :param heap:
    :return:
    """
    res = []
    for i in range(len(heap)):
        length = len(heap)
        heap[0], heap[length-1] = heap[length-1], heap[0]
        res.append(heap.pop(-1))
        adjust_min_heap(heap, 0)

    return res


def findKthNum(nums, k):
    """
    获取nums数组中第k大的元素
    :param nums:
    :param k:
    :return:
    """
    target = len(nums) - k

    left, right = 0, len(nums)-1

    while True:
        partition_index = get_index(nums, left, right)

        if partition_index == target:
            return nums[partition_index]
        elif partition_index > target:
            right = partition_index - 1
        else:
            left = partition_index + 1


def get_index(nums, left, right):
    """
    快排思想 返回partition_index, 使得左边小 右边大
    :param nums:
    :param left:
    :param right:
    :return:
    """

    pivot = nums[left]

    while left < right:

        while left < right and nums[right] >= pivot:
            right -= 1

        nums[left] = nums[right]

        while left < right and nums[left] <= pivot:
            left += 1

        nums[right] = nums[left]

    nums[left] = pivot

    return left


if __name__ == '__main__':
    nums = [34, 22, 9, 5, 68, 71, 78, 23]
    target = findKthNum(nums, 6)
    target_res = findKthNumWithHeap(nums, 6)
    print(target)
    print(target_res)

