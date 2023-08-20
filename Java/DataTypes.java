import java.io.*;

class DataTypes
{
	public static void main(String[] args) throws IOException
	{
		InputStreamReader inObj = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(inObj);

		System.out.println("Data Types");
		System.out.println("\nInteger, Float, Boolean, String\n");
    /*
		Integer Number = 99;
		Double Float = 99.99;
		Boolean t = true;
		String string = "Characters";

		System.out.println(Number);
		System.out.println(Float);
		System.out.println(t);
		System.out.println(string);
    */
		System.out.println("Enter Integer Value : ");
		Integer n = Integer.parseInt(in.readLine());
		System.out.println("Int is : "+n);

		System.out.println("Enter Float Value : ");
		Double f = Double.parseDouble(in.readLine());
		System.out.println("Float is : "+f);
		
		System.out.println("Enter Any Strings : ");
		String s = in.readLine();
		System.out.println("String is : "+s);

	}
}
