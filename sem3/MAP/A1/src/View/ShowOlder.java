package View;
import Controller.Controller;
import Model.BasicAnimal;

import java.util.Arrays;

public class ShowOlder extends Command {
    public ShowOlder(Controller controller) {
        super(controller);
    }

    @Override
    public void execute() {
        BasicAnimal[] olderAnimals = controller.getOlderAnimals();

        for (BasicAnimal animal : olderAnimals) {
            if (animal != null) {
                System.out.println(animal);
            }
        }
    }
}
