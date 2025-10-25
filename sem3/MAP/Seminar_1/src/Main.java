import items.Apple;
import items.Book;
import items.Item;
import items.WeightedItem;

import java.util.Arrays;
import java.util.List;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws Exception {
        var repository = new Repository();

        var book = new Book(25, "Alba ca Zapada");
        var apple = new Apple(55);

        repository.addItem(apple);
        repository.addItem(book);

        List<WeightedItem> objects = repository.getItems();

        for (WeightedItem object : objects) {
            try{
                IO.println(object.getWeight());
            }
            catch (NullPointerException e){
                IO.println(e.getMessage());
                throw new Exception();
            }

            if (object instanceof Book book2) {
                IO.println(book2.getTitle());
            }
        }

        IO.println(objects);
    }
}