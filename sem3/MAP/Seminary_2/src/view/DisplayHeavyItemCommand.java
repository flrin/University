package view;

import controller.Controller;

public class DisplayHeavyItemCommand extends Command {

    public DisplayHeavyItemCommand(Controller controller) {
        super(controller);
    }

    @Override
    public void execute() {
        for (var item : controller.getHeavyItems(200)) {
            IO.println(item);
        }
    }
}
