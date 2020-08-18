import java.util.Scanner;

public class Multiply_2588 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int result=0;
        int[] n2_array = new int[3];
        for (int i = 0; i < n2_array.length; i++) {
            n2_array[i]=n2%10;
            n2=n2/10;
        }
        for (int i=0; i<n2_array.length;i++){
            int temp=n1*n2_array[i];
            System.out.println(temp);
            for (int j=0;j<i;j++){
                temp=temp*10;
            }
            result+=temp;
        }
        System.out.println(result);
    }
}
