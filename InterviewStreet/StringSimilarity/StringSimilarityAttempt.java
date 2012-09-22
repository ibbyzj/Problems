import java.util.Scanner;

//Lesson learnt, Java char arrays work faster than python ><, strangely for Interview Street brute force worked o.0
public class StringSimilarityAttempt {

	public static void main(String [] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		for (int m = 0 ; m < N; m++) {
			char[] charString = in.next().toCharArray();
			int sum = 0;
			for(int i = 0; i < charString.length; i++ ) {
				for( int j = i, tempIndex = 0 ; j < charString.length; j++,sum++,tempIndex++) {
					if(charString[j] != charString[tempIndex]) 
						break;
				}
			}
			System.out.println(sum);
		}
	}
}
