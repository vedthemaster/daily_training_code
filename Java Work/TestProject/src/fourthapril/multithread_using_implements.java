package fourthapril;


public class multithread_using_implements implements Runnable {
    public void run(){
        System.out.println("Current Thread: "+ Thread.currentThread().getId());

    }
    public static void main(String[] args) {
        multithread_using_extend abc = new multithread_using_extend();
        for(int i =0;i<6;i++){
            Thread a = new Thread(abc);
    
            a.start();
        }

    }
    
}
