package model;

import java.util.Arrays;

public class Box implements Item {
    private final Item[] items;

    public Box(Item[] items) {
        this.items = items;
    }

    @Override
    public String toString() {
        return "Box{" +
                "items=" + Arrays.toString(items) +
                '}';
    }

    @Override
    public int getWeight() {
        int totalWeight = 0;
        for (Item item : items) {
            totalWeight += item.getWeight();
        }
        return totalWeight;
    }
}
