package firstapril;
import java.util.Scanner;

public class throws_exception {


    public static int t_expec(int a, int b) throws ArithmeticException,IndexOutOfBoundsException{
        int arr[]= new int[5];
        if(a==0){
            throw new ArithmeticException("Can not be zero");
        }else if (b>arr.length){
            throw new IndexOutOfBoundsException("Array Index out of bound");
        }
        else{

            int c = 25/a;
            return c;
        }
        
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int cd = sc.nextInt();
        int dc = sc.nextInt();
        try{

            int ans =  t_expec(cd, dc);
            System.out.println(ans);
        }catch(ArithmeticException c){
            System.out.println(c.getMessage());
        }
        catch(IndexOutOfBoundsException d){
            System.out.println(d.getMessage());
            
        }
        
        
    }
    
}
