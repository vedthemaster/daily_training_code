abstract class Pen{

    public  abstract void  write();
    public abstract void refill();

}
class fountain_pen extends Pen{
    public String name1;
    public void write(){
        System.out.println("This is Write");
        
    }
    public void refill(){
        System.out.println("This is refill");
        
    }
    public void change_nib(){
        System.out.println("This is Chnage Nib");

    }
    fountain_pen(String name){
        name1 =name;

    }

}
// abstract class pensil extends Pen{

// }

public class task2_abstraction {

    public static void main(String[] args){
        fountain_pen obj = new fountain_pen("pen1");
        obj.change_nib();
        obj.write();
        obj.refill();

    }
    
}
