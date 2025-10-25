package repository;

import model.Item;

import java.util.Arrays;

public class ArrayRepository implements Repository {
    private final Item[] items;
    private int size = 0;

    public ArrayRepository(int capacity) {
        this.items = new Item[capacity];
    }

    @Override
    public void add(Item item) {
        if (size == items.length) {
            throw new RepositoryFullException();
        }

        items[size++] = item;
    }

    @Override
    public Item[] getAll() {
        return Arrays.copyOf(items, size);
    }

    // Object
    // Throwable
    // Exception  -- checked exception
    // RuntimeException  -- unchecked exception

    @Override
    public Item remove(int index) throws IndexOutOfBoundsException {
        if (index < 0 || index >= items.length) {
            throw new IndexOutOfBoundsException();
        }

        var removedItem = items[index];
        for(int i = index; i < size; i++) {
            items[i] = items[i+1];
        }

        size--;
        return removedItem;
    }
}
