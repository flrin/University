package Repository;
import Model.BasicAnimal;

public interface Repository {
    public BasicAnimal[] getAll();
    public void add(BasicAnimal animal) throws RepositoryException;
    public void remove(String name);
}
