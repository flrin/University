package View;
import Model.BasicAnimal;
import Model.Fish;
import Model.Turtle;
import Controller.Controller;
import Controller.AddException;

public class AddCommand extends Command {
    private final String[] parts;

    public AddCommand(Controller controller, String[] parts) {
        super(controller);
        this.parts = parts;
    }

    @Override
    public void execute() throws ViewException {
        if (parts.length != 3) {
            throw new LengthException("Length should be " + 3);
        }

        String type = parts[0].toLowerCase().trim();
        String name = parts[1];
        String strAge = parts[2];

        int age;

        try{
            age = Integer.parseInt(strAge);
        }
        catch(Exception e){
            throw new InputException("Inavild Age");
        }

        BasicAnimal animal = switch (type) {
            case "fish" -> new Fish(name, age);
            case "turtle" -> new Turtle(name, age);
            default -> null;
        };

        if (animal != null) {
            controller.addAnimal(animal);
        }
        else
            IO.println("Wrong animal type");
    }
}
