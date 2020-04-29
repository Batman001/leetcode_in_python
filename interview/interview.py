# -*- coding:utf-8 -*-
from linkedlist_relate.ReverstListNode import ListNode, \
    create_linked_list, print_linked_list


def merge_linked_list(head1, head2):
    """
    归并排序head1链表和head2链表
    :param head1: 链表head1的头结点
    :param head2: 链表head1的头结点
    :return: 排序后的头结点
    """
    new_head = ListNode(0)
    cur_node = new_head

    while head1 and head2:
        if head1.val < head2.val:
            cur_node.next = head1
            head1 = head1.next
            cur_node = cur_node.next

        else:
            cur_node.next = head2
            head2 = head2.next
            cur_node = cur_node.next
    if head1:
        cur_node.next = head1
    else:
        cur_node.next = head2
    return new_head.next


def sum_linked_list(head1, head2):
    """
    对两个链表上下进行求和 如果超过10 则进1
    input:
    head1: 1->9->3->2
    head2: 2->5->4->8
    output:
    new_head 3->4->8->0->1

    :param head1:
    :param head2:
    :return:
    """
    new_head = ListNode(0)
    cur_node = new_head

    # 使用全局变量存储上次剩余值
    last_res = 0
    while head1 and head2:
        cur_sum = head1.val + head2.val + last_res

        if cur_sum < 10:
            cur_node.next = ListNode(cur_sum)
            cur_node = cur_node.next
            last_res = 0
        else:
            cur_node.next = ListNode(cur_sum % 10)
            cur_node = cur_node.next
            last_res = cur_sum // 10

        head1 = head1.next
        head2 = head2.next

    if last_res != 0:
        cur_node.next = ListNode(last_res)
    return new_head.next


def quick_sort(array, left, right):
    while left < right:
        middle_index = get_middle_index(array, left, right)
        quick_sort(array, left, middle_index-1)
        quick_sort(array, middle_index+1, right)


def get_middle_index(array, left, right):
    pivot = array[left]
    while left < right:

        while left < right and array[right] > pivot:
            right -= 1

        array[left] = array[right]

        while left < right and array[left] < pivot:
            left += 1
        array[right] = array[left]

    array[left] = pivot

    return left


def search_in_dup(array, target):
    """
    查找target在有序数组array中的位置 返回第一个出现的位置
    :param array: 有序递增数组
    :param target: 待查找数
    :return: 第一个出现的位置
    """
    left, right = 0, len(array)-1
    while left <= right:
        mid = (left+right) // 2
        if target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid - 1
        # 向左寻找第一个出现的位置
        else:
            if mid - 1 > 0 and array[mid-1] == array[mid]:
                mid -= 1
            return mid

    return -1


class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.heap_size = len(array)

    def build_heap(self):
        for i in range(self.heap_size // 2 -1, -1, -1):
            self.min_adjust(i)

    def min_adjust(self, index):
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        min_index = index
        if left_index < self.heap_size and self.heap[left_index] < self.heap[index]:
            min_index = left_index
        if right_index < self.heap_size and self.heap[right_index] < self.heap[min_index]:
            min_index = right_index

        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self.min_adjust(min_index)

    def heap_sort(self):
        for i in range(len(self.heap)):
            self.heap[0], self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
            self.heap_size -= 1
            self.min_adjust(0)


if __name__ == "__main__":
    head1 = create_linked_list([2, 3, 5, 7, 8])
    head2 = create_linked_list([1, 4, 7, 9, 10])

    res = merge_linked_list(head1, head2)
    print_linked_list(res)
    print()

    head3 = create_linked_list([1, 6, 8, 12, 9])
    head4 = create_linked_list([4, 6, 9, 7, 23])
    res_sum = sum_linked_list(head3, head4)
    print_linked_list(res_sum)
    print()

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

