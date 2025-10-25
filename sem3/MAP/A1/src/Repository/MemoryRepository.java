package Repository;
import Model.BasicAnimal;

import java.util.Objects;

public class MemoryRepository implements Repository {
    private final BasicAnimal[] animals = new BasicAnimal[10];
    private int count = 0;

    public MemoryRepository() {
    }

    public BasicAnimal[] getAll() {
        return animals;
    }

    public void add(BasicAnimal animal) throws RepositoryException{
        if (count == animals.length) {
            throw new RepoFullException("Repository is full!");
        }

        for (BasicAnimal basicAnimal : animals) {
            if (basicAnimal != null && Objects.equals(basicAnimal.getAnimalName(), animal.getAnimalName())) {
                throw new AnimalExistsException("Animal already exists!");
            }
        }

        animals[++count] = animal;
    }

    public void remove(String name) {
        for (int i = 0; i < count; i++) {
            if (animals[i] == null) continue;

            if (Objects.equals(animals[i].getAnimalName(), name)) {
                for (int j = i + 1; j < count; j++) {
                    animals[j - 1] = animals[j];
                }
                count--;
                animals[count] = null;
                return;
            }
        }

        // throw exception

    }
}
