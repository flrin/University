package model;

public class BasicItem implements Item {
    protected int weight;

    public BasicItem(int weight) {
        if (weight <= 0) {
            throw new IllegalArgumentException("Weight must be positive");
        }

        this.weight = weight;
    }

    @Override
    public int getWeight() {
        return weight;
    }
}
