package View;

import Controller.*;

import java.util.Arrays;

public class View {
    private final Controller controller;
    public View(Controller controller) {
        this.controller = controller;
    }

    public void run(){

        while(true){
            String input = IO.readln(">>");
            String[] parts = input.split(" ");

            try{

                switch (parts[0]){
                    case "add":
                        AddCommand command = new AddCommand(controller,
                                Arrays.copyOfRange(parts, 1, parts.length));
                        command.execute();
                        break;

                    case "remove":
                        RemoveCommand command2 = new RemoveCommand(controller,
                                Arrays.copyOfRange(parts, 1, parts.length));
                        command2.execute();
                        break;

                    case "older":
                        ShowOlder command3 = new ShowOlder(controller);
                        command3.execute();
                        break;

                    case "exit":
                        System.exit(0);
                }

            }
            catch(Exception e){
                System.out.println(e.getMessage());
            }
        }
    }
}
