package repository;


import model.Item;

public interface Repository {
    void add(Item item);
    Item[] getAll();
    Item remove(int index) throws IndexOutOfBoundsException ;
}
