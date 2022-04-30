package april6;
import java.util.*;

public class hashset_operation {
    public static void main(String[] args) {

        Integer [] i = {33,5,65,8,9,12};
        Integer [] j = {3,5,56,86,96,12};

        Set<Integer> ns =  new HashSet<>(Arrays.asList(i));
        Set<Integer> n1s = new HashSet<>(Arrays.asList(j));
        Set<Integer> nu =  new HashSet<>();
        Set<Integer> ni =  new HashSet<>();
        Set<Integer> nd =  new HashSet<>();

        nu.addAll(ns);
        nu.addAll(n1s);

        ni.addAll(ns);
        ni.retainAll(n1s);

        nd.addAll(ns);
        nd.removeAll(n1s);

        System.out.println(ns);
        System.out.println(n1s);
        System.out.println(nu);
        System.out.println(ni);
        System.out.println(nd);
    }
    
}
