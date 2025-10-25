import java.util.ArrayList;

public class MeUtils {
    public static int utilityUsage = 0;

    public static ArrayList<Integer> stringSequenceToInt(String string) {
        String[] stringValues = string.split("\\s+");

        ArrayList<Integer> intValues = new ArrayList<>();
        for (String stringValue : stringValues) {
            int value;

            try{
                value = Integer.parseInt(stringValue);
            }
            catch(NumberFormatException e){
                continue;
            }

            intValues.add(value);
        }

        utilityUsage++;
        return intValues;
    }

    @Override
    public String toString() {
        return "General personal Utilities Class";
    }
}
