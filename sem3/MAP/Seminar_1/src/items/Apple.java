package items;

public class Apple extends Item {
    public Apple(int weight) {
        super(weight);
    }

    @Override
    public String toString() {
        return "items.Apple " + this.weight + "kg";
    }
}
