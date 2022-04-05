import java.time.*;
import java.util.*;
public class Task2_date {

    public static void main(String[] args){
        LocalDate today = LocalDate.now();
        System.out.println("today's date is: " + today);
        
        LocalDate birth = LocalDate.of(2001,3,3);
        System.out.println(Period.between(birth, today).getYears());


    }
    
}
