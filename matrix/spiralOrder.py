# leetcode59 回环打印矩阵（顺时针方向）

def spiralOrder(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  # 取矩阵第一行并删除
        matrix = list(zip(*matrix))[::-1]  # 旋转矩阵
    return result


def spiral_order(matrix):
    """
    务必记住边界判断条件
    left > right 或者 top > bottom
    :param matrix:
    :return:
    """
    rows, cols = len(matrix), len(matrix[0])
    left, right, top, bottom = 0, cols-1, 0, rows-1
    res = []
    while True:
        if left > right:
            break
        # 从左到右打印
        for i in range(left, right+1, 1):
            res.append(matrix[top][i])
        top += 1

        # 从上到下打印
        if top > bottom:
            break
        for i in range(top, bottom+1, 1):
            res.append(matrix[i][right])
        right -= 1

        # 从右向左打印
        if left > right:
            break
        for i in range(right, left-1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1

        # 从下向上打印
        if top > bottom:
            break
        for i in range(top, bottom-1, -1):
            res.append(matrix[i][left])
        left += 1

    return res


def generate_matrix(n):
    """
    leetcode59. 螺旋矩阵 II  https://leetcode.cn/problems/spiral-matrix-ii/
    :param n: 给你一个正整数 n
    :return: 生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix
    """
    num, num_end = 1, n*n
    left, right, top, bottom = 0, n-1, 0, n-1
    res = [[_ for _ in range(n)] for _ in range(n)]

    while num <= num_end:
        # left -> right
        for i in range(left, right+1):
            res[top][i] = num
            num += 1
        top += 1

        # top -> bottom
        for i in range(top, bottom+1):
            res[i][right] = num
            num += 1
        right -= 1

        # right -> left
        for i in range(right, left-1, -1):
            res[bottom][i] = num
            num += 1
        bottom -= 1

        # bottom -> top
        for i in range(bottom, top-1, -1):
            res[i][left] = num
            num += 1
        left += 1

    return res


if __name__ == '__main__':
    aa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    aa_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    bb = spiralOrder(aa)
    cc = spiral_order(aa_)
    print("旋转矩阵遍历二维矩阵后的结果为：", bb)
    print("left->right + top->bottom + right->left + bottom->top 遍历二维矩阵后的结果为：", cc)

    n = 3
    print("顺时针生成的矩阵为：", generate_matrix(n))
