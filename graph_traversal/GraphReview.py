# -*- coding:utf-8 -*-
# 参考博文：https://blog.csdn.net/u011519550/article/details/89056393


class Vertex:
    """
    顶点类
    """
    def __init__(self, num):
        self.id = num
        self.connectedTo = []
        self.color = 'white'
        self.dist = 0

    def addNeighbor(self, nbr):
        self.connectedTo.append(nbr)

    def setColor(self, color):
        """
        通过颜色表征顶点的类型
        :param color:  开始顶点color为black， 其余顶点为white
        :return:
        """
        self.color = color

    def setDistance(self, dist):
        self.dist = dist

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def __str__(self):
        return str(self.id) + "  color: " + self.color + "  dist: " + str(
            self.dist) + '  connectedTo:' + str(
            [x.id for x in self.connectedTo])


class Graph:
    """
    图的类
    """
    def __init__(self):
        # 存放所有顶点
        self.vertexes = {}

    def addVertex(self, key):
        new_vertex = Vertex(key)
        self.vertexes[key] = new_vertex
        return new_vertex

    def getVertex(self, n):
        return self.vertexes.get(n)

    def __iter__(self):
        return iter(self.vertexes.values())


def bfs_max_path(start):
    """
    图的广度遍历 使用队列实现，并通过动态规划实现最长路径（从start节点开始到结束节点的最长路径）
    :param start: 开始节点
    :return: 返回最长路径长度 以及 经过的路径信息
    """
    start.setDistance(1)
    distance = 1
    # 使用vertex_queue广度遍历
    vertex_queue = [start]
    seen = set()
    seen.add(start)

    # 动态规划实现开始节点的最长路径
    while len(vertex_queue) > 0:
        curr_vertex = vertex_queue.pop(0)
        for nbr in curr_vertex.connectedTo:
            nbr.setDistance(curr_vertex.getDistance() + 1)
            if nbr not in seen:
                vertex_queue.append(nbr)
                seen.add(nbr)

        # 动态求解最长路径长度的推导公式
        if distance < curr_vertex.getDistance():
            distance = curr_vertex.getDistance()

    return distance


def bfs_min_path(gra, start, end):
    """
    图的广度遍历 使用队列实现，并通过动态规划实现最短路径（从start节点开始到 end节点的最长路径）
    :param gra: 待计算图
    :param start: 开始节点
    :param end: 结束节点
    :return: 最短长度
    """
    start_v = gra.getVertex(start)
    start_v.setDistance(1)
    vertex_queue = [start_v]

    while len(vertex_queue) > 0:
        curr_vertex = vertex_queue.pop(0)

        if curr_vertex.id == end:
            # print(curr_vertex.dist)
            return curr_vertex.dist
        for nbr in curr_vertex.connectedTo:
            if nbr not in vertex_queue:
                nbr.setDistance(curr_vertex.getDistance() + 1)
                vertex_queue.append(nbr)


def bfs_all_path(gra, start, end):
    """
    计算两点之间的全部路径总数
    :param gra: 图
    :param start: 起始顶点
    :param end: 结束顶点
    :return: 返回总的路径条数
    """
    start_v = gra.getVertex(start)

    count = 0
    start_v.setDistance(1)
    vertex_queue = [start_v]
    while len(vertex_queue) > 0:
        curr_vertex = vertex_queue.pop(0)

        if curr_vertex.id == end:
            count += 1
        for nbr in curr_vertex.connectedTo:
            nbr.setDistance(curr_vertex.getDistance() + 1)
            vertex_queue.append(nbr)
    return count


if __name__ == "__main__":
    # a, b, c, d, e, f, g, h, i, j = range(1, 11)
    # 测试图结构
    graph_dict = {
        1: [2, 3],
        2: [3],
        3: [4, 5, 6],
        4: [7],
        5: [10],
        6: [8, 10],
        7: [10],
        8: [9],
        9: [10],
        10: [],
    }

    graph = Graph()
    n = 0
    # 设置graph的key
    for key, value in graph_dict.items():
        vertex = graph.addVertex(key)
        if n == 0:
            vertex.setColor('black')
        n += 1
    # 生成graph全部邻接节点
    for key, values in graph_dict.items():
        vertex = graph.getVertex(key)
        for value in values:
            ner_vertexes = graph.getVertex(value)
            vertex.addNeighbor(ner_vertexes)

    print('graph.vertexes.keys():', graph.vertexes.keys())
    print(graph.vertexes.get(6))

    longest_path = bfs_max_path(graph.vertexes.get(1))
    print("其路径最长长度为%d" % longest_path)
    print("从1到4的最短路径长度为 %d" % (bfs_min_path(graph, 1, 10)))

