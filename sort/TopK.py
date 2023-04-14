# -*- coding:utf-8 -*-

# 维护一个k大的小根堆
import random


def build_heap(array, k):
    array = array[:k]
    for i in range(int(k/2)-1, -1, -1):
        minify(array, i)
    return array


def minify(array, i):
    left = left_index(i)
    right = right_index(i)
    length = len(array)
    if left < length and array[left] < array[i]:
        smallest = left
    else:
        smallest = i
    if right < length and array[right] < array[smallest]:
        smallest = right

    if smallest == i or smallest >= length:
        return
    array[i], array[smallest] = array[smallest], array[i]
    minify(array, smallest)


def heap_sort(heap):
    result = []
    for i in range(len(heap)):
        heap_size = len(heap)
        heap[0], heap[heap_size - 1] = heap[heap_size -1], heap[0]
        result.append(heap.pop())
        minify(heap, 0)
    return result


def left_index(i):
    return 2*i+1


def right_index(i):
    return 2*i+2


def get_top_k(array, k):
    heap = build_heap(array, k)
    for i in range(k, len(array)):
        if array[i] <= heap[0]:
            continue
        else:
            heap[0] = array[i]
            minify(heap, 0)
    return heap


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def main():
    array = random_int_list(-1000, 1000, 40)
    print(array)
    heap = get_top_k(array, 9)
    result = heap_sort(heap)
    # 由于result中值为从小到大排列，然后对数字进行整理后输出
    result = result[::-1]
    print(result)


if __name__ == "__main__":
    main()

