import controller.Controller;
import model.*;
import repository.ArrayRepository;
import repository.Repository;

void main() {
    Repository repo = new ArrayRepository(10);
    Controller controller = new Controller(repo);

    controller.addItem(new Apple(150));
    controller.addItem(new Apple(200));
    controller.addItem(new Cake(250));
    controller.addItem(new Cake(300));
    controller.addItem(new Book(200));
    controller.addItem(new Book(300));
    controller.addItem(new Box(new Item[]{
            new Apple(100),
            new Cake(150),
            new Book(200),
            new Box(new Item[]{
                new Apple(50),
                new Cake(75),
                new Book(100)
            })
    }));
    for(Item item : controller.getHeavyItems(200)) {
        IO.println("Item weight: " + item.getWeight());
    }

}