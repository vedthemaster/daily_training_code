interface TVremote{

    public void test();
    
}
interface smartTVremote extends TVremote{
    public void test();
    
}

class TV implements smartTVremote{
    public void test(){
        System.out.println("This is TV class");
    };

}

public class task3_interfaces {

    public static void main(String[] args){
        System.out.println("This is main");
        TV newTv = new TV();
        newTv.test();
    }
    
}
