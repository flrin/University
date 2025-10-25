package Model;

public class Fish extends BasicAnimal {

    public Fish(String name, int age) {
        super(name, age);
    }

    @Override
    public String toString() {
        return "Fish {" + super.toString() + "}";
    }
}
