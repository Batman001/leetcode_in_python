class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        result = head
        change_len = n - m + 1
        new_head = None
        pre_head = None
        # 第一次调整head指针的时候还要记录调整区域的前趋，用temp动态保存
        for i in range(1, m):
            pre_head = head
            head = head.next

        modify_list_tail = head

        while (change_len > 0 and head != None):
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
            change_len -= 1

        modify_list_tail.next = head
        if (pre_head != None):
            pre_head.next = new_head
        else:
            result = new_head
        return result

