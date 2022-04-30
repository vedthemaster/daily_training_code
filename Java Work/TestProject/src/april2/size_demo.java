package april2;
import java.io.File;

public class size_demo {

    public static void main(String[] args) {
        File file1= new File("demo.txt");
        double size = file1.length();
        System.out.println(size);

        double ksize = size/1024;
        double msize = ksize/1024;
        System.out.println(ksize + " Kilo");
        System.out.println(msize + " Mega");
    }
    
}
