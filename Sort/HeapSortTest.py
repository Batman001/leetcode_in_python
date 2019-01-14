#-*- coding:utf-8 -*-
'''
小根堆
(1) 堆创建过程
(2) 堆排序过程（将堆尾元素与堆头元素交换，递归动态调整堆 使堆始终保持小根堆性质）
(3) 动态调整堆过程(保证父节点的值始终小于左右孩子节点值)


'''

def build_heap(array):
    length = len(array);
    for i in range(int(length/2) - 1, -1,-1):
        Minify(array, i)
    return array


def heap_sort(array):
    result = []
    for i in range(len(array)):
        length = len(array)
        array[0], array[length-1] = array[length-1], array[0]
        result.append(array.pop())
        Minify(array, 0)
    return result


def Left(i):
    return i*2 + 1

def Right(i):
    return i*2 + 2


def Minify(array, i):
    left = Left(i)
    right = Right(i)
    length = len(array)
    if(left < length and array[left]<array[i]):
        smallest = left
    else:
        smallest = i
    if(right < length and array[right] < array[smallest]):
        smallest = right

    if(smallest == i or smallest >= length):
        return
    array[i], array[smallest] = array[smallest], array[i]
    Minify(array, smallest)

def main():
    heap = [3,9,5,20,34,-4,8,89]
    heap = build_heap(heap)
    print(heap)

    sort_result = heap_sort(heap)
    print(sort_result)


if __name__ == "__main__":
    main()