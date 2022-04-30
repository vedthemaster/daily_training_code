package april6;
import java.util.*;


public class queue_operation {
    public static void main(String[] args) {

         Queue<String> nQueue = new LinkedList<>();
         Queue<String> n1Queue = new LinkedList<>();
         nQueue.offer("One");
         nQueue.offer("Two");
         nQueue.offer("Three");
         nQueue.offer("Four");
         System.out.println(nQueue);
  
         while(nQueue.size()!=1){
           n1Queue.offer(nQueue.peek());
           nQueue.remove();

        }
        System.out.println(n1Queue);
            

    }
    
}
