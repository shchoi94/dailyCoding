package p14888;

import java.util.ArrayList;
import java.util.Scanner;

class Operation {
	private String origin;
	String now;

	Operation(String origin) {
		this.origin = origin;
		this.now = origin;
	}

	public String getNow() {return now;}

	public void setNowUsed() { this.now = "used"; }

	public void setNowOrigin() { this.now = this.origin; }

	public String getOrigin() { return origin; }

}

class P14888 {
	int n;
	ArrayList<Integer> inputList = new ArrayList<>();
	ArrayList<Integer> opQuantityList = new ArrayList<>();
	ArrayList<Operation> opList = new ArrayList<>();
	ArrayList<Integer> resultList = new ArrayList<>();

	public void solve() {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();


		for (int i = 0; i < n; i++) {
			inputList.add(sc.nextInt());
		}
		for (int i = 0; i < 4; i++) {
//           idx 0,1,2,3 -> +,-,*,/ value is number of operation
			opQuantityList.add(sc.nextInt());
		}
		opList = makeOperationList();
//		op list 연산자 출력
//		for (int i = 0; i < opList.size(); i++) {
//			System.out.println(opList.get(i).getOrigin());
//		}
		dfs(0);
//		System.out.println(resultList);
		System.out.println(maxValue());
		System.out.println(minValue());


	}

	public ArrayList<Operation> makeOperationList() {
		for (int i = 0; i < opQuantityList.get(0); i++) {
			opList.add(new Operation("+"));
		}
		for (int i = 0; i < opQuantityList.get(1); i++) {
			opList.add(new Operation("-"));
		}
		for (int i = 0; i < opQuantityList.get(2); i++) {
			opList.add(new Operation("*"));
		}
		for (int i = 0; i < opQuantityList.get(3); i++) {
			opList.add(new Operation("/"));
		}
		return opList;
	}
	public int calculation(String op,int num1, int num2){
		switch (op){
			case "+":
				return num1+num2;
			case "-":
				return num1-num2;
			case "*":
				return num1*num2;
			case "/":
				return num1/num2;
		}
		return 0;
	}
	public void dfs(int depth) {
		if (depth == n - 1)
			resultList.add(inputList.get(n - 1));
		for (int i = 0; i < opList.size(); i++) {
			if(opList.get(i).getNow().equals(opList.get(i).getOrigin())){
				int temp=inputList.get(depth+1);
				inputList.set(depth+1,calculation(opList.get(i).getNow(),inputList.get(depth),inputList.get(depth+1)));
				opList.get(i).setNowUsed();
				dfs(depth+1);
				opList.get(i).setNowOrigin();
				inputList.set(depth+1,temp);
			}
		}
	}
	public int maxValue(){
		int max=resultList.get(0);
		for(int i=1; i<resultList.size();i++){
			if(max<resultList.get(i)){ max=resultList.get(i); }
		}
		return max;
	}
	public int minValue(){
		int min=resultList.get(0);
		for(int i=1; i<resultList.size();i++){
			if(min>resultList.get(i)){ min=resultList.get(i); }
		}
		return min;
	}
}

public class Main {
	public static void main(String[] args) {
		P14888 p14888 = new P14888();
		p14888.solve();
	}
}
