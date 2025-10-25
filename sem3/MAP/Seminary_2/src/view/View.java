package view;

import controller.Controller;

import java.util.Arrays;

public class View {
    private final Controller controller;

    public View(Controller controller) {
        this.controller = controller;
    }
    public void run() {
        while (true) {
            String input = IO.readln("Insert command: ");
            String[] parts = input.split(" ");
            switch (parts[0]) {
                case "add":
                    Command command = new AddBasicItemCommand(controller,
                            Arrays.copyOfRange(parts, 1, parts.length));
                    command.execute();
                    break;
                case "display":
                    Command command2 = new DisplayHeavyItemCommand(controller);
                    command2.execute();
                    break;
                case "exit":
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Unknown command.");
            }
        }
    }
}
