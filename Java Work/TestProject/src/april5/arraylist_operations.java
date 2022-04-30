package april5;

import java.util.ArrayList;
import java.util.function.Predicate;

public class arraylist_operations {
    public static void main(String[] args) {
        ArrayList<String> nArrayList = new ArrayList<String>();
        ArrayList<String> scriptinglanguage = new ArrayList<String>();
        System.out.println(nArrayList.isEmpty());
        
        // nArrayList.add("Google");
        // nArrayList.add("Apple");
        // nArrayList.add("Microsoft");
        // nArrayList.add("Amazon");
        // nArrayList.add("Facebook");
        
        // System.out.println("Best company: "+ nArrayList.get(3));
        // System.out.println("Second Best company: "+ nArrayList.get(0));
        // System.out.println("Last company in the list : "+ nArrayList.get(4));
        // System.out.println("Last company in the list : "+ nArrayList.get(nArrayList.size()-1));
        // nArrayList.set(2, "eInfochips");

        nArrayList.add("C");
        nArrayList.add("C++");
        nArrayList.add("Java");
        nArrayList.add("Python");
        nArrayList.add("Kotlin");
        nArrayList.add("Perl");
        nArrayList.add("Ruby");

        scriptinglanguage.add("Python");
        scriptinglanguage.add("Ruby");

        System.out.println(nArrayList);
        System.out.println(nArrayList.size());
        nArrayList.remove(5);
        System.out.println(nArrayList);
        nArrayList.remove("Kotlin");
        System.out.println(nArrayList);
        nArrayList.removeAll(scriptinglanguage);
        System.out.println(nArrayList);
        nArrayList.removeIf(j -> j.charAt(0) == 'C');
        System.out.println(nArrayList);
        nArrayList.clear();
        System.out.println(nArrayList);

    }
    
}
