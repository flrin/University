package Repository;

public class AnimalExistsException extends RepositoryException {
    public AnimalExistsException(String message) {
        super(message);
    }
}
