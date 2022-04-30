package april5;
import java.util.*;

public class stack_operation {

    static void getsize(int a){
        if(a==5){
            System.out.println("Stack is overflow");

        }
        else if(a==-1){
            System.out.println("Stack is underflow");

        }
        else{
            System.out.println("Stack is normal");

        }

    }

    public static void main(String[] args) {
        Stack<Integer> nstack = new Stack<>();
        // nstack.setSize(5);
        
        System.out.print(nstack);
        System.out.println(nstack.isEmpty());
        nstack.push(10);
        nstack.push(20);
        nstack.push(30);
        nstack.push(40);
        int c_size =nstack.size();
        getsize(c_size);

        nstack.push(50);
        c_size =nstack.size();
        getsize(c_size);
        // nstack.push(60);
        System.out.println(nstack);
        System.out.println(nstack.isEmpty());
        nstack.pop();
        nstack.pop();
        nstack.pop();
        nstack.pop();
        System.out.println(nstack.peek());
        nstack.pop();
        c_size =nstack.size();
        System.out.println(c_size);
        getsize(c_size);
        System.out.println(nstack);
        System.out.println(nstack.search(20));



        
    }
    
}
