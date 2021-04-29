public class Driver {
    public static void main(String[] args) {
        BinaryTree<String> t1 = new BinaryTree<>("1");
        BinaryTree<String> t2 = new BinaryTree<>("2");
        BinaryTree<String> t3 = new BinaryTree<>("3");
        BinaryTree<String> t4 = new BinaryTree<>("4");
        BinaryTree<String> t5 = new BinaryTree<>("5");
        BinaryTree<String> t6 = new BinaryTree<>("6");
        BinaryTree<String> t7 = new BinaryTree<>("7");

        t2.addLeftChild(t4);
        t2.addRightChild(t5);
        t3.addLeftChild(t6);
        t3.addRightChild(t7);
        t1.addLeftChild(t2);
        t1.addRightChild(t3);

        for (String t : t1)
            System.out.println(t);
    }
}
