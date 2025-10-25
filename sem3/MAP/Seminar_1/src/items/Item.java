package items;

public class Item implements WeightedItem {
    public final int weight;

    protected Item (int weight) {
        this.weight = weight;
    }

    public int getWeight() {
        return weight;
    }
}
