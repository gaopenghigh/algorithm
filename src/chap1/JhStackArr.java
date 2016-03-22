package chap1;

import java.util.Iterator;

/**
 * use array to implement stack
 * Created by gaopeng on 3/22/16.
 */
public class JhStackArr<T> implements Iterable<T> {
    private int N = 0;
    private T[] elements = (T[]) new Object[1];

    public boolean isEmpty() {
        return N == 0;
    }

    public int size() {
        return N;
    }

    private void resize(int newSize) {
        T[] tmp = (T[]) new Object[newSize];
        for (int i = 0; i < N; i++) {
            tmp[i] = elements[i];
        }
        elements = tmp;
    }

    @Override
    public Iterator<T> iterator() {
        return new JhStackArrIterator();
    }

    private class JhStackArrIterator implements Iterator<T> {

        private int i = N;

        @Override
        public boolean hasNext() {
            return i > 0;
        }

        @Override
        public T next() {
            return elements[--i];
        }
    }

    public void push(T e) {
        if (elements.length == N) {
            resize(N * 2);
        }
        elements[N++] = e;
    }

    public T pop() {
        T e = elements[--N];
        if (N > 0 && N == elements.length/4) {
            resize(elements.length/2);
        }
        return e;
    }

    public static void main(String[] args) {
        JhStackArr<Integer> s = new JhStackArr<Integer>();
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
