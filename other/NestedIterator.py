# -*- coding:utf-8 -*-
class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here
        :type nestedList : List[NestedInteger]
        :param nestedList:
        """
        self.flat = []

        def flatten(nested):
            for n in nested:
                if n.isInteger():
                    self.flat.append(n)
                else:
                    flatten(n.getList())
        flatten(nestedList)
        self.flat = self.flat[::-1]

    def next(self):
        """
        :return: int
        """
        return self.flat.pop()

    @staticmethod
    def hasNext(self):
        """
        :return: bool
        """
        return bool(self.flat)


if __name__ == "__main__":
    n = NestedIterator([1,2,[2,3,[4,7,8]]])
    print(n)
