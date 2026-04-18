class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list(array):
    """
    通过array实现链表的构建
    input： [1,2,3,4,5]
    output: 1->2->3->4->5
    :param array:
    :return:
    """
    head = ListNode(array[0])
    cur_node = head
    for item in array[1:]:
        cur_node.next = ListNode(item)
        cur_node = cur_node.next
    return head


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


def reverse(head):
    if head is None:
        return head
    cur_node = head
    pre_node = None
    while cur_node:
        next_node = cur_node.next
        cur_node.next = pre_node
        pre_node = cur_node
        cur_node = next_node

    return pre_node


def print_linked_list(head):
    while head:
        print(str(head.val), end="->")
        head = head.next


if __name__ == "__main__":
    s = Solution()
    head = create_linked_list([2, 7, 8, 3, 5])
    print("本身链表为:")
    print_linked_list(head)
    # result = s.next_larger_nodes(head)
    reverse_result = reverse(head)
    print()
    print("链表逆置的结果为：")
    print_linked_list(reverse_result)
