package secondapril;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Filewriter_demo {
    public static void main(String[] args) {
        try {
            FileWriter myWriter = new FileWriter("demo.txt");
            myWriter.write("Java is a Secure and reliable too");
            myWriter.close();
            } catch (IOException e) {
            System.out.println("error");
            }
            File file = new File("demo.txt");
            
            try(FileReader fr=new FileReader(file))
            {
            int content;
            while((content=fr.read())!=-1) {
            System.out.print((char) content);
            }
            }catch(IOException e){
            e.printStackTrace();
            }

        
        }    
}
