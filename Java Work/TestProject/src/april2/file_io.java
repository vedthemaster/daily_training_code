package april2;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class file_io {

    public static void main(String[] args) {

        final String fileName = "demo.txt";
        try{
            File demo =  new File(fileName);
            if(demo.exists() == false){
                if(demo.createNewFile()){
                    System.out.println("File created successfully");
                }
            }else{
                System.out.println("Failed");
                System.exit(0);
            }

            Scanner sc =new Scanner(System.in);
            System.out.println("Enter text into file: ");
            String text = sc.nextLine();
            int val;
            FileOutputStream fileOut = new FileOutputStream(demo);
    
            fileOut.write(text.getBytes());
            fileOut.flush();
            fileOut.close();
            FileInputStream filein = new FileInputStream(demo);
            System.out.println("Content of file is: ");
            while((val=filein.read())!=-1){
                System.out.println((char)val);
            }

        }catch(Exception e){
            System.out.println(e);
        }

        


       
    }
    
}
