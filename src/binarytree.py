class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def add_leftchild(self, tree):
        if not isinstance(tree.data, type(self.data)) and (self.data is not None):
            raise TypeError("TypeError: Type mismatch between " + type(self.data).__name__ + " and " +
                            type(tree.data).__name__)

        self.left = tree

    def add_rightchild(self, tree):
        if not isinstance(tree.data, type(self.data)) and (self.data is not None):
            raise TypeError("TypeError: Type mismatch between " + type(self.data).__name__ + " and " +
                            type(tree.data).__name__)

        self.right = tree


if __name__ == "__main__":
    t1 = BinaryTree(0)
    t1.add_leftchild(BinaryTree(5))
    t2 = BinaryTree(10)
    t2.add_rightchild(BinaryTree("not an int"))
    t1.add_rightchild(t2)
