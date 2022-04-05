interface A {

    public void show();

}
class B implements A {
    public void show(){
        System.out.println("This is B");
    }

}
interface I extends A {

}
class D extends B implements I{

}

public class task4_multiple_inheritance {
    public static void main (String[] args){

    }
    
}
