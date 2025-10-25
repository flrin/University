package model;

public class Cake extends BasicItem {
    public Cake(int weight) {
        super(weight);
    }

    @Override
    public String toString() {
        return "Cake{" +
                "weight=" + weight +
                '}';
    }
}
