package april1;

import java.util.Scanner;



public class custom_exception {
    public static  int multi(int a,int b){
 
            if(a ==0 || b == 0 ){
               throw new ArithmeticException("Can not be zero");
                                
            }else{
                return a*b;              
            }  

    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int u_a = sc.nextInt();
        int u_b = sc.nextInt();
        try{
   

            int c = multi(u_a,u_b);
            System.out.println(c);
            
        }catch(ArithmeticException e){
            System.out.println(e.getMessage());
        }

        
    }
    
}
