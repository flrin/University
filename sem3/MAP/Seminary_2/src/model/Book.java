package model;

public class Book extends BasicItem {
    public Book(int weight) {
        super(weight);
    }

    @Override
    public String toString() {
        return "Book{" +
                "weight=" + weight +
                '}';
    }
}
