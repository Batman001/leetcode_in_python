# -*- coding:utf-8 -*-

import random
'''
建立堆大小为K的堆
'''
def build_heap(array,k):
    array = array[:k]
    for i in range(int(k/2),-1,-1):
        Minify(array, i)
    return array

def Minify(array, i):
    length = len(array)
    left = Left(i)
    right = Right(i)
    if(left < length and array[left]<array[i]):
        smallest = left
    else: smallest = i
    if(right < length and array[right]<array[smallest]):
        smallest = right
    if(smallest == i or smallest >= length):
        return
    array[i], array[smallest] = array[smallest], array[i]
    Minify(array, smallest)


def heap_sort_output(heap):
    result = []
    for i in range(len(heap)):
        heap_size = len(heap)
        heap[0], heap[heap_size-1] = heap[heap_size -1], heap[0]
        result.append(heap.pop())  #此时由于最小值交换到堆尾，所以直接pop方法得到最小值
        Minify(heap, 0)
    return result



def Left(i):
    return 2*i+1

def Right(i):
    return 2*i+2


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

def main(array, k):
    length = len(array)
    heap = build_heap(array, k)
    for i in range(k,length):
        if(array[i]<=heap[0]):
            continue
        else:
            heap[0] = array[i]
            Minify(heap, 0)
    result = heap_sort_output(heap)
    result = result[::-1]
    print(result)

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8,9,10,34,25,564,683,26,675]
    main(array, 9)