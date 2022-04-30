package april6;
import java.util.*;

public class hashtable_operation {
    public static void main(String[] args) {

        Hashtable<String,Integer> ht =  new Hashtable<>();

        ht.put("Red", 1);
        ht.put("White", 2);
        ht.put("Blue", 3);
        ht.put("Black", 4);
        ht.put("Green", 5);

        System.out.println(ht.values()+ " "+ht.keySet());

        if(ht.keySet().contains("Green")){
            System.out.println(ht.get("Green"));
        }
        System.out.println(ht.keySet().contains("Orange")); 
      
   
        


        
    }
    
}
