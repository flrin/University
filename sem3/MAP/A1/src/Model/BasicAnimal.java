package Model;

public class BasicAnimal implements Animal {
    private final int age;
    private final String name;
    public BasicAnimal(String name, int age) {
        this.age = age;
        this.name = name;
    }

    @Override
    public int getAge() {
        return age;
    }

    @Override
    public String getAnimalName() {
        return name;
    }

    @Override
    public String toString() {
        return name + " " + age;
    }
}
