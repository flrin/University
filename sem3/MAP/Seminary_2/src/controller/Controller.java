package controller;

import model.Item;
import repository.Repository;

import java.util.Arrays;

public class Controller {
    private final Repository repository;

    public Controller(Repository repository) {
        this.repository = repository;
    }

    public void addItem(Item item) {
        repository.add(item);
    }

    public Item removeItem(int index) {
        return repository.remove(index);
    }

    public Item[] getHeavyItems(double weightLimit) {
        Item[] items = repository.getAll();
        Item[] heavyItems = new Item[items.length];
        int size = 0;

        for (Item item : items) {
            if (item.getWeight() > weightLimit) {
                heavyItems[size++] = item;
            }
        }

        return Arrays.copyOf(heavyItems, size);
    }
}
