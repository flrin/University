package View;

import Controller.Controller;

public abstract class Command {
    protected final Controller controller;
    public Command(Controller controller) {
        this.controller = controller;
    }
    public abstract void execute() throws ViewException;
}
