# -*- coding:utf-8 -*-


def BFS(graph, s):
    """
    图的广度遍历 使用队列进行实现 主要体现在 queue.pop(0) 确定为队列的存储结构
    :param graph: 广度遍历的图
    :param s: 开始的节点
    :return:
    """
    queue = [s]
    # seen 用于存储已经看到过的节点 使用集合进行存储
    seen = set()
    seen.add(s)
    # 使用parent 存储当前节点的上一个节点
    parent = {s: None}
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = vertex
        print(vertex)
    return parent


def DFS(graph, s):
    """
    图的深度遍历 使用队列进行实现 主要体现在 queue.pop() 使用存储结构为stack
    :param graph: 广度遍历的图
    :param s: 开始的节点
    :return:
    """
    stack = [s]
    # seen 用于存储已经看到过的节点 使用集合进行存储
    seen = set()
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex)


def cal_shortest_path(parent, end):
    """
    根据parent的字典存储结构 返回从遍历开始节点(parent中value为None的key)到end的路径信息
    :param parent: 存储当前节点以及当前节点的父节点信息
    :param end: 终止节点
    :return:
    """
    while end is not None:
        print(end)
        end = parent[end]


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]
    }
    # BFS(graph, "E")
    print("当前图广度遍历的结果为：")
    parent = BFS(graph, "A")

    # 打印parent
    print("当前图广度遍历后并存储相关节点的附近节点的信息为：")
    for key in parent.keys():
        print(key, parent[key])
    print("计算从F节点到开始节点的最短路径为：")
    cal_shortest_path(parent, "F")





