class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def add_leftchild(self, tree):
        if tree.data is None:
            self.left = tree

        elif not isinstance(tree.data, type(self.data)) and (self.data is not None):
            raise TypeError("TypeError: Type mismatch between " + type(self.data).__name__ + " and " +
                            type(tree.data).__name__)

        self.left = tree

    def add_rightchild(self, tree):
        if tree.data is None:
            self.left = tree

        elif not isinstance(tree.data, type(self.data)) and (self.data is not None):
            raise TypeError("TypeError: Type mismatch between " + type(self.data).__name__ + " and " +
                            type(tree.data).__name__)

        self.right = tree

    def __iter__(self):
        yield self.data
        if self.left is not None:
            for d in self.left.__iter__():
                yield d
        if self.right is not None:
            for d in self.right.__iter__():
                yield d


# if __name__ == "__main__":
#     t1 = BinaryTree(1)
#     t2 = BinaryTree(2)
#     t3 = BinaryTree(3)
#     t4 = BinaryTree(4)
#     t5 = BinaryTree(5)
#     t6 = BinaryTree(6)
#     t7 = BinaryTree(None)
#
#     t2.add_leftchild(t4)
#     t2.add_rightchild(t5)
#     t3.add_leftchild(t6)
#     t3.add_rightchild(t7)
#     t1.add_leftchild(t2)
#     t1.add_rightchild(t3)
#
#     print(list(iter(t1)))
