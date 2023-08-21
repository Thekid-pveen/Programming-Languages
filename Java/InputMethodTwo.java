import java.io.*;

class InputMethodTwo
{
    public static void main(String[] args) throws IOException
    {
        DataInputStream in = new DataInputStream(System.in);
       
        //BufferedReader

        System.out.println("\n-______________________________-");

        System.out.println("\nEnter Any String : ");
        String s = in.readLine();
        System.out.println("\nYour Input String is_ "+s);

        System.out.println("\nEnter Any Integer : ");
        Integer n = Integer.parseInt(in.readLine());
        System.out.println("\nYour Integer is_ "+n);

        System.out.println("\nEnter Any Float : ");
        Double f = Double.parseDouble(in.readLine());
        System.out.println("\nYour Float is : "+f);

        System.out.println("\n-________________________________-");
    }
}
