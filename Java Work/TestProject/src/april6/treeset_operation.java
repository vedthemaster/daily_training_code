package april6;
import java.util.*;

public class treeset_operation {
    public static void main(String[] args) {
        
        Integer [] i = {33,5,65,8,9,12,5,41,42,85};
        Set<Integer> ts = new TreeSet<>(Arrays.asList(i));
        Set<Integer> hs = new HashSet<>();
        Set<Integer> ls = new LinkedHashSet<>();
        

        hs.add(4785);
        hs.addAll(ts);
        hs.add(96);
        ls.add(855);
        ls.add(748);

        ls.addAll(ts);
        System.out.println(ts);
        System.out.println(hs);
        System.out.println(ls);

    }
    
}
