package model;

public class Apple extends BasicItem {
    public Apple(int weight) {
        super(weight);
    }

    @Override
    public String toString() {
        return "Apple{" +
                "weight=" + weight +
                '}';
    }
}
