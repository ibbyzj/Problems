import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


public class Median {
public static void main(String [] args) {
	
	Scanner in = new Scanner(System.in);
	//Read the number of lines in input
	long N = in.nextLong();
	
	ArrayList<Long> sortedList = new ArrayList<Long>();
	//Keep looping till for each entry and make changes to the Arraylist
	for(int i=0; i<N; i++){
		String op = in.next();
		long number = in.nextLong();
		doIt(op, number, sortedList);
		}
		}

	
public static void doIt(String input, long number, ArrayList<Long>sortedList) {
	
	int index = Collections.binarySearch(sortedList, number);
	
	if(input.equals("a")) {
		//If element is not present add it
		if(index<0) {
			sortedList.add(-index-1,number);
		}
		//If it is present add it on the existing index
		else {
			sortedList.add(index,number);
		}
		
	}
	
	else {
		//If index is not present print Wrong!
		if(index<0) {
			System.out.println("Wrong!");
			return;
		}
		//Remove the element if it is present, only removes a single value
		else {
			sortedList.remove(index);
		}
	
	}
	
	
	//If list is empty after removing print Wrong!
	if(sortedList.size() == 0) {
		System.out.println("Wrong!");
		return;
	}
	//If the number of elements in the list is odd then print the middle element
	if(sortedList.size()%2 != 0) {
		if(sortedList.size() == 1) {
		System.out.println((long)sortedList.get(0));	
		}
		else {
		System.out.println((long)sortedList.get(sortedList.size()/2));
		}
	}
	
	//Print the median of the two middle elements ( String format to format large numbers )
	else {
		double numby = (( (long)(sortedList.get(sortedList.size()/2) + (long)sortedList.get((sortedList.size()/2)-1)) ));
		if (numby%2 == 0) {
			System.out.println((long)numby/2);
		}
		else {
			String truncated = String.format("%.1f", numby/2);
			truncated = truncated.substring(0,truncated.length());
			System.out.println(truncated);
		}
	}
}
}
