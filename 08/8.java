import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class main
{
    public static void main(String[] args)
    {
        String input = "";
        int max = 0;
        File inputFile = new File("input.txt");
        try
        {
            Scanner inputScanner = new Scanner(inputFile);
            input = inputScanner.nextLine();
            inputScanner.close();
        }
        catch (FileNotFoundException error)
        {
            error.printStackTrace();
        }
        for (int i = 0 ; i < input.length() - 5 ; i++)
        {
            int tmp = 1;
            for (int j = i ; j < i + 5 ; j++)
                tmp *= Character.getNumericValue(input.charAt(j));
            max = tmp > max ? tmp : max;
        }
        System.out.println("" + max);
    }
}
