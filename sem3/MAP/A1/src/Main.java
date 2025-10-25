import Model.Fish;
import Model.Turtle;
import View.View;
import Controller.Controller;
import Repository.MemoryRepository;


/// 8. Intr-un acvariu traiesc pesti si broaste testoase.
/// Sa se afiseze toate vietuitoarele din acvariu care sunt
/// mai batrine de 1 an.



//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        MemoryRepository memoryRepository = new MemoryRepository();

        Turtle turtle = new Turtle("Joe", 25);
        Turtle turtle2 = new Turtle("Mike", 3);
        Fish fish = new Fish("Fischer", 1);

        try{
            memoryRepository.add(turtle);
            memoryRepository.add(turtle2);
            memoryRepository.add(fish);
        }
        catch (Exception e){}

        Controller controller = new Controller(memoryRepository);
        View view = new View(controller);
        view.run();
    }
}