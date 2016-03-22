package chap1;

import java.util.Iterator;

/**
 * queue
 * Created by gaopeng on 3/22/16.
 */
public class JhQueue<T> implements Iterable<T> {

    private class Node {
        T item;
        Node next;
    }

    private Node first;
    private Node last;
    private int N = 0;

    public boolean isEmpty() {
        return N == 0;
    }

    public void enqueue(T e) {
        Node oldLast = last;
        Node n = new Node();
        n.item = e;
        n.next = null;
        if (isEmpty()) {
            first = last = n;
        } else {
            last = n;
            oldLast.next = last;
        }
        N++;
    }

    public T dequeue() {
        T e = first.item;
        first = first.next;
        N--;
        if (isEmpty()) {
            last = null;
        }
        return e;
    }

    @Override
    public Iterator<T> iterator() {
        return new JhQueueIterator();
    }

    private class JhQueueIterator implements Iterator<T> {
        private Node current = first;

        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public T next() {
            T e = current.item;
            current = current.next;
            return e;
        }
    }

    public static void main(String[] argv) {
        JhQueue<Integer> q = new JhQueue<Integer>();
        q.enqueue(1);
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.enqueue(1);
        q.enqueue(1);
        for (Integer i: q) {
            System.out.printf("%d,", i);
        }
        System.out.println();
        System.out.printf("dequeue %d\n", q.dequeue());
        System.out.printf("dequeue %d\n", q.dequeue());
        System.out.printf("dequeue %d\n", q.dequeue());
        System.out.printf("dequeue %d\n", q.dequeue());
        System.out.printf("dequeue %d\n", q.dequeue());
        System.out.printf("dequeue %d\n", q.dequeue());
        System.out.printf("dequeue %d\n", q.dequeue());
        System.out.printf("dequeue %d\n", q.dequeue());
        System.out.printf("dequeue %d\n", q.dequeue());
    }
}
