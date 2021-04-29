import java.util.*;

public class BinaryTree<T> implements Iterable<T> {
    private T data;
    private BinaryTree<T> left;
    private BinaryTree<T> right;

    // Default values of Objects is null anyway, do nothing
    public BinaryTree() { }

    public BinaryTree(T data) {
        this.data = data;
    }

    public void addLeftChild(BinaryTree<T> tree) {
        left = tree;
    }

    public void addRightChild(BinaryTree<T> tree) {
        right = tree;
    }

    @Override
    public Iterator<T> iterator() {
        return new BinaryTreeIterator(this);
    }

    private class BinaryTreeIterator implements Iterator<T> {
        private LinkedList<BinaryTree<T>> queue = new LinkedList<>();

        BinaryTreeIterator(BinaryTree<T> tree) {
            if (tree.data != null)
                queue.add(tree);
        }

        @Override
        public boolean hasNext() {
            return !queue.isEmpty();
        }

        @Override
        public T next() {
            if (!hasNext())
                throw new NoSuchElementException();

            BinaryTree<T> tree = queue.remove();
            if (tree.left != null)
                queue.add(tree.left);
            if (tree.right != null)
                queue.add(tree.right);

            return tree.data;
        }
    }
}
