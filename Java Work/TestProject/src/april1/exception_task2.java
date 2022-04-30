package april1;

import java.util.Scanner;

class ExceptionLineTooLong extends Exception{
    public ExceptionLineTooLong(String s){
        super(s);

    }
}

public class exception_task2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String strt = sc.nextLine();
        int lenstr = strt.length();
        try{
            if (lenstr > 10){
                throw new ExceptionLineTooLong("The string is too long");
            }else{
                System.out.println("String accepted");
            }
        }catch(ExceptionLineTooLong c){
            System.out.println(c.getMessage()); 
        }
    }
    
}
