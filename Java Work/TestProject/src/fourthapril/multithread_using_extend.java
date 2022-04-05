package fourthapril;

public class multithread_using_extend extends Thread {
    public void run(){
        System.out.println("Thread is running: "+Thread.currentThread().getId() );
        System.out.println("Thread's Priority is: "+Thread.currentThread().getPriority() );
        System.out.println("Thread's Name is: "+Thread.currentThread().getName() );
        try{
            Thread.sleep(1000);
        }catch(InterruptedException ie){
            System.out.println("thread 2");
        }
    }

    public static void main(String[] args) {

        // for(int i=0;i<10;i++){

        //     multithread_using_extend th = new multithread_using_extend();
        //     th.start();
        // }


        // JOIN and IsAlive

        multithread_using_extend t1 = new multithread_using_extend();
        multithread_using_extend t2 = new multithread_using_extend();
        multithread_using_extend t3 = new multithread_using_extend();

        t2.setPriority(Thread.MAX_PRIORITY);
        t2.setPriority(Thread.MIN_PRIORITY);
        t1.start();
        try{
            t1.join();
        }catch(Exception e){
            System.out.println(e);
        }
        t2.start();
        t3.start();
        System.out.println(t1.isAlive());
        System.out.println(t2.isAlive());
        System.out.println(t3.isAlive());
        try{
            t2.join();
        }catch(Exception e){
            System.out.println(e);
        }
        try{
            t3.join();
        }catch(Exception e){
            System.out.println(e);
        }
        System.out.println(t1.isAlive());
        System.out.println(t2.isAlive());
        System.out.println(t3.isAlive());
        // System.out.println(t1);
        // System.out.println(t2);
        // System.out.println(t3);

    }
    
}
