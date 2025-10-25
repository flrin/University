import java.util.ArrayList;

public class MeUtilsMath extends MeUtils {
    public static final double PI = 3.14159265358979323846;

    public MeUtilsMath() {
        super();
    }

    public static int meanFromIntArray(ArrayList<Integer> array){
        int sum = 0;
        for (int value : array) {
            sum += value;
        }

        utilityUsage++;
        return sum/array.size();
    }

    @Override
    public String toString(){
        return "Mathematical personal Utilities class";
    }
}
