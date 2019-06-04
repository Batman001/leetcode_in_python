# -*- coding:utf-8 -*-

from linkedlist_relate.ReverstListNode import ListNode


class Solution:

    def reverse_k_group(self, head, k):
        """
        leetcode 25. K 个一组翻转链表
        :param head: ListNode 链表的表头
        :param k: 每个翻转的个数
        :return: 翻转后链表的表头
        """
        if k <= 1:
            return head
        p = head

        # Get the length of LinkedList
        length = 0
        while p is not None:
            length += 1
            p = p.next

        cnt = 0
        cur_node = head

        while cur_node is not None:
            if cnt + k <= length:
                # 如果是第一次翻转链表
                if cnt == 0:
                    head = self.reverse_k(cur_node, k)
                    cnt += k
                # 如果不是第一次翻转链表
                else:
                    # 首先得到第一次翻转后 cur_node的下一个节点
                    next_node = cur_node.next
                    # 从next_node 开始 翻转k个节点 得到翻转后的新表头
                    new_head = self.reverse_k(next_node, k)
                    # cur_node为上一次翻转后的尾节点 将上次翻转的尾节点与本次翻转的表头进行连接
                    cur_node.next = new_head
                    # 移动cur_node 到本次翻转的尾节点处
                    cur_node = next_node
                    cnt += k
            else:
                break
        return head

    @staticmethod
    def reverse_k(self, head, k):
        """
        对以head为表头的链表进行翻转k个节点 返回翻转后表头
        :param head: 链表表头
        :param k: k个节点
        :return: 翻转后的表头
        """
        pre = None
        cur_node = head
        reverse_tail = head
        count = 1

        while count <= k:
            next_node = cur_node.next
            cur_node.next = pre
            pre = cur_node
            cur_node = next_node
            reverse_tail = next_node
            count += 1

        head.next = reverse_tail
        return pre

    @staticmethod
    def print_list_node(self, head):
        """
        打印链表的方法
        :param head: 链表表头
        :return: 控制台打印链表
        """
        cur_node = head
        while cur_node is not None:
            print(str(cur_node.val) + "->", end='')
            cur_node = cur_node.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    res = s.reverse_k_group(head, 5)
    s.print_list_node(res)


