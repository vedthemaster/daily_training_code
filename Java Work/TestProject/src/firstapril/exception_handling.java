package firstapril;

public class exception_handling {
    public static void main(String[] args) {
        try{

            int arr[] = new int[5];
            arr[6] = 30/1;
            // String text = null;
            // System.out.println(text.length());
        }
        catch(ArithmeticException e){
            
            System.out.println("Number exception");
        }
        catch(ArrayIndexOutOfBoundsException t){
            System.out.println("Array exception");
        }
        catch(NullPointerException c){
            System.out.println("Null exception");      
        }
        catch(Exception g){
            System.out.println("Common Exception");

        }
    }
    
}
