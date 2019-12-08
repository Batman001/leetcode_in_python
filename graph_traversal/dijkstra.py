# -*- coding:utf-8 -*-
import heapq
import math


def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph.keys():
        if vertex != s:
            distance[vertex] = math.inf
    return distance


def dijkstra(graph, s):
    """
    图的广度遍历 使用队列进行实现 主要体现在 queue.pop(0) 确定为队列的存储结构
    :param graph: 广度遍历的图
    :param s: 开始的节点
    :return:
    """
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    # seen 用于存储已经看到过的节点 使用集合进行存储
    seen = set()

    # 使用parent 存储当前节点的上一个节点
    distance = init_distance(graph, s)

    parent = {s: None}
    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for node in nodes:
            if node not in seen:
                if dist + graph[vertex][node] < distance[node]:
                    heapq.heappush(pqueue, (dist + graph[vertex][node], node))
                    parent[node] = vertex
                    distance[node] = dist + graph[vertex][node]
        print(vertex)

    return parent, distance


if __name__ == "__main__":
    graph = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6}
    }
    parent, distance = dijkstra(graph, "A")
    print(parent)
    print(distance)
