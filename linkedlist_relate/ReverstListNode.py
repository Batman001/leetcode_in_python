class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    @staticmethod
    def reverse_between(self, head, m, n):
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

        while change_len > 0 and head != None:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
            change_len -= 1

        modify_list_tail.next = head
        if pre_head != None:
            pre_head.next = new_head
        else:
            result = new_head
        return result

    @staticmethod
    def next_larger_nodes(self, head):
        """
        参考链接：https://blog.csdn.net/fuxuemingzhu/article/details/89048785
        链表中的下一个更大节点（请注意是下一个更大节点 而不是全部节点中最大)
        示例1：
        输入：[2,1,5]
        输出：[5,5,0]
        示例2：
        输入：[2,7,4,3,5]
        输出：[7,0,5,5,0]
        示例3：
        输入：[1,7,5,1,9,2,5,1]
        输出：[7,9,9,9,0,5,0,0]
        :param head: 头指针
        :return:返回列表
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        stack = []
        res = [0 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(i)

        return res


if __name__ == "__main__":
    s = Solution()
    head = ListNode(2)
    head.next = ListNode(7)
    head.next.next = ListNode(8)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(5)
    result = s.next_larger_nodes(head)
    print(result)



