
def spiralOrder(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  # 取矩阵第一行并删除
        matrix = list(zip(*matrix))[::-1]  # 旋转矩阵
    return result


def spiral_order(matrix):
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


if __name__ == '__main__':
    aa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    aa_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    bb = spiralOrder(aa)
    cc = spiral_order(aa_)
    print(bb)
    print(cc)