package view;

import controller.Controller;
import model.Apple;
import model.Book;
import model.Cake;

public class AddBasicItemCommand extends Command {
    private final String[] input;

    public AddBasicItemCommand(Controller controller, String[] input) {
        super(controller);
        this.input = input;
    }

    @Override
    public void execute() {
        switch (input[0]) {
            case "cake" -> {
                int weight = Integer.parseInt(input[1]);
                controller.addItem(new Cake(weight));
            }
            case "book" -> {
                int weight = Integer.parseInt(input[1]);
                controller.addItem(new Book(weight));
            }
            case "apple" -> {
                int weight = Integer.parseInt(input[1]);
                controller.addItem(new Apple(weight));
            }
            default -> System.out.println("Unknown item type: " + input[0]);
        }
    }
}
