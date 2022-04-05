 class Caller {
    static int stCount = 0;
    public int count = 0;

    public  int getCount(){
        return count;
    }
    public static int getStCount(){
        // System.out.println("Test");
        return stCount;
    }
    Caller(){
        count ++;
        stCount ++;
    }   
}
 class Task4 extends Caller{
     
    public static void main(String[] args){

        Caller c1 = new Caller();
        Caller c2 = new Caller();
        Caller c3 = new Caller();
        Caller c4 = new Caller();
        Caller c5 = new Caller();
        int f_count = c5.getCount();
        int f_stcount = c5.getStCount();
        System.out.println(f_count + " "+ f_stcount);


        // Task4.getCount();
     }
 }