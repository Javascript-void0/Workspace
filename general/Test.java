package general;
public class Test {
	
	public static void main(String[] args) {
		
		int a = 5;
		char b = 'i';
		long c = 400;
		double d = 3.2;
		
		String name = "Java";
		System.out.println(name.toUpperCase());
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		System.out.println(d);
		
		String exclaim = addExclamationPoint(name);
		System.out.println(exclaim);
		
		String test = turnToTest(name);
		System.out.println(test);
		System.out.println(name.toUpperCase());

		while(a < 50) {
			System.out.println(a);
			a++;
		}

	}
	
	public static String test() {
		return "Testing";
	}

	public static String addExclamationPoint(String s) {
		return s + "!";
	}
	
	public static String turnToTest(String s) {
		return "Test";

	}

}
