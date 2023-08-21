import java.io.*;
import java.util.*;

class InputMethodThree
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        /*
          In this file working not correctly, But works
        */
        System.out.println("-_____________________________-");
        
        System.out.println("\nEnter Any String : ");
        String s = in.next();
        System.out.println("\nYour String is_ "+s);

        System.out.println("\nEnter Any Integer : ");
        Integer n = in.nextInt();
        System.out.println("\nYour Input Integer is_ "+n);

        System.out.println("\nEnter Any Float : ");
        Double f = in.nextDouble();
        System.out.println("\nYour Input Float is_ "+f);

        System.out.println("-_________________________________-");
    }
}
