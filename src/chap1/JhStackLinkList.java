package chap1;

import java.util.Iterator;

/**
 * Stack structure
 * Created by gaopeng on 3/12/16.
 */
public class JhStackLinkList<T> implements Iterable<T> {

    private JhNode first;
    private int N;

    @Override
    public Iterator<T> iterator() {
        return new JhStackIterator();
    }

    private class JhStackIterator implements Iterator<T> {
        private JhNode current = first;

        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public T next() {
            T item = current.item;
            current = current.next;
            return item;
        }
    }

    /**
     * Stack Node
     */
    private class JhNode {
        public T item;
        public JhNode next;
    }

    public boolean isEmpty() {
        return first == null;
    }

    public int size() {
        return N;
    }

    public void push(T item) {
        JhNode n = new JhNode();
        n.item = item;
        n.next = first;
        first = n;
        N++;
    }

    public T pop() {
        N--;
        T item = first.item;
        first = first.next;
        return item;
    }

    public static void main(String[] args) {
        JhStackLinkList<Integer> s = new JhStackLinkList<Integer>();
        for (int i=0; i<=9; i++) {
            s.push(i);
        }

        Iterator<Integer> iter = s.iterator();
        while (iter.hasNext()) {
            Integer i = iter.next();
            System.out.printf("%d,", i);
        }
        System.out.println();
        System.out.printf("pop %d\n", s.pop());
        System.out.printf("pop %d\n", s.pop());
        System.out.printf("push %d\n", 3);
        s.push(3);
        System.out.printf("pop %d\n", s.pop());

        while (!s.isEmpty()) {
            System.out.printf("pop %d\n", s.pop());
        }
    }
}
