package april5;

import java.util.*;

public class vector_operation {
    public static void main(String[] args) {
        Vector<String> nVector = new Vector<>();
        Vector<String> n1Vector = new Vector<>();
        Vector<String> n2Vector = new Vector<>();

        nVector.add("Cricket");
        nVector.add("Football");
        nVector.add("Baseball");
        nVector.add("Hockey");
        nVector.add("Volleyball");

        System.out.println(nVector);

        n1Vector.add("Cricket");
        n1Vector.add("Football");
        n1Vector.add("Baseball");

        n2Vector.add("Cricket");
        n2Vector.add("Football");
        n2Vector.add("Baseball");
        n2Vector.add("Tennis");

        Collections.sort(nVector);

        System.out.println(nVector);
        System.out.println(n1Vector);
        
        System.out.println(nVector.containsAll(n1Vector));
        System.out.println(nVector.containsAll(n2Vector));
       
    }
  
}


