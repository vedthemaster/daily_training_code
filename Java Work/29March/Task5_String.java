
public class Task5_String {
    public static void main(String[] args){
        String name = "Ved Jagdishkumar Patel";
 
        char f = name.charAt(0);
        System.out.print(f);
      


        for (int i=0;i< name.length();i++){

            if (name.charAt(i) == ' '){
                  char a= name.charAt(i+1);
                  System.out.print(a);

            }

        }

    }
    
}
