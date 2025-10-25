package Controller;
import Model.BasicAnimal;
import Repository.Repository;

public class Controller {
    private final Repository repository;
    public Controller(Repository repository) {
        this.repository = repository;
    }

    public BasicAnimal[] getOlderAnimals() {
        BasicAnimal[] animals = repository.getAll();
        BasicAnimal[] olderAnimals = new BasicAnimal[animals.length];
        int olderAnimalIndex = 0;
        for (BasicAnimal animal : animals) {
            if (animal == null) {
                continue;
            }
            if (animal.getAge() > 1){
                olderAnimals[olderAnimalIndex++] = animal;
            }
        }
        return olderAnimals;
    }

    public void addAnimal(BasicAnimal animal) {
        try{
            repository.add(animal);
        }
        catch (Exception e){

        }
    }

    public void removeAnimal(String name) {
        repository.remove(name);
    }

}
