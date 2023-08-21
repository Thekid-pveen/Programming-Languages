import java.io.*;

class InputMethodOne
{
    public static void main(String[] args) throws IOException
    {
        InputStreamReader InputObj = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(InputObj);

        System.out.println("\n-_____________________________-");
        
        System.out.println("\nEnter Any String : ");
        String s = in.readLine();
        System.out.println("\n Your Input String is_ "+s);

        System.out.println("\nEnter Any Integer : ");
        Integer n = Integer.parseInt(in.readLine());
        System.out.println("\nYour Input Integer is_ "+n);

        System.out.println("\nEnter Any Float : ");
        Double f = Double.parseDouble(in.readLine());
        System.out.println("\nYour Input Float is_ "+f);

        System.out.println("\n-________________________________-");
    }
}
