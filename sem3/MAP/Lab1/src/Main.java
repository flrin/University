import java.util.ArrayList;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        MeUtils utils = new MeUtils();
        MeUtilsMath utilsMath = new MeUtilsMath();

        IO.println(MeUtils.utilityUsage);

        ArrayList<Integer> intValues = MeUtils.stringSequenceToInt(input);
        int mean = MeUtilsMath.meanFromIntArray(intValues);

        IO.println(mean);
        IO.println(utils);
        IO.println(utilsMath);
        IO.println(MeUtilsMath.utilityUsage);
        IO.println(MeUtilsMath.PI);
    }
}