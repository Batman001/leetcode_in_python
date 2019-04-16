# -*- coding:utf-8 -*-

'''
从下到上遍历调整根节点（即含有左右子树的节点,从 int(n/2)-1 索引开始到 0
'''
def build_heap(heap):
    heap_size = len(heap)
    for i in range(int(heap_size/2)-1,-1,-1):       #循环至root根节点结束
        maxModify(heap, i)

'''
heap_sort方法遍历n次，每次将heap的堆尾元素与堆头元素进行替换
然后调整堆头元素
'''
def heap_sort(heap):
    result = []
    for i in range(len(heap)):
        heap_size = len(heap)
        heap[0],heap[heap_size-1] = heap[heap_size-1],heap[0]
        result.append(heap.pop())
        maxModify(heap, 0)
    return result


'''
maxify方法动态调整堆，使得堆始终保持根节点的值大于左右孩子节点值
结束条件： 如果largest等于i说明i是最大元素 或者 largest超出heap范围 说明不存在比i节点大的孩子节点

调整完当前根节点之后，递归调用maxify方法
直到最小值
'''


def maxModify(heap, i):
    heap_size = len(heap)
    left = Left(i)
    right = Right(i)

    if(left<heap_size and heap[left] > heap[i]):
        largest = left
    else:
        largest = i
    if (right<heap_size and heap[right] > heap[largest]):
        largest = right
    if(largest == i or largest >= heap_size):
        return
    temp = heap[i]
    heap[i] = heap[largest]
    heap[largest] = temp
    maxModify(heap, largest)


'''
左子树索引为：当前索引 i*2 + 1
'''

def Left(i):
    return 2*i+1

'''
右子树索引为：当前索引 i*2 + 2
'''
def Right(i):
    return 2*i+2

'''
堆排序过程：
（1）构建堆 时间复杂度o(n)
（2）调整堆 时间复杂度o(logn)
遍历全部节点与堆头元素交换,时间复杂度为o(n)
然后动态调整堆时间复杂度o(logn)
（3) 整体时间复杂度为o(n + nlogn)
'''
def main():
    heap = [1, 3, 78, 34, 10, 9, 2, 5, -8, 9, 34, 76, 89, 12]
    build_heap(heap)
    heap = heap_sort(heap)
    # 此时排好序的列表为从大到小排列
    heap = heap[::-1]
    print(heap)

if __name__ == "__main__":
    main()


def minWindow(self, s, t):
    count1 = {}
    count2 = {}
    for char in t:
        if char not in count1:
            count1[char] = 1
            count2[char] = 1
        else:
            count1[char] += 1
            count2[char] += 1
    count = len(t)
    start = 0
    minSize = len(s) + 1
    minStart = 0

    for end in range(len(s)):
        if s[end] in count2 and count2[s[end]] > 0:
            count1[s[end]] -= 1
            if count1[s[end]] >= 0:
                count -= 1
            if count == 0:
                while True:
                    if s[start] in count2 and count2[s[start]] > 0:
                        if count1[s[start]] < 0:
                            count1[s[start]] += 1
                        else:
                            break
                    start += 1
                if minSize > end - start + 1:
                    minSize = end - start + 1
                    minStart = start
    if minSize < len(s) + 1:
        return s[minStart:minStart + minSize]
    else:
        return ""