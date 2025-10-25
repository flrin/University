package Model;

public class Turtle extends BasicAnimal {

    public Turtle(String name, int age) {
        super(name, age);
    }

    @Override
    public String toString() {
        return "Turtle {" + super.toString() + "}";
    }

}