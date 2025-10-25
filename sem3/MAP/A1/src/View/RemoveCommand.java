package View;
import Controller.Controller;

public class RemoveCommand extends Command {
    private final String[] parts;

    public RemoveCommand(Controller controller, String[] parts) {
        super(controller);
        this.parts = parts;
    }

    @Override
    public void execute() throws LengthException {
        if (parts.length != 1) {
            throw new LengthException("Length should be 1");
        }

        String name = parts[0];


        controller.removeAnimal(name);
    }
}
