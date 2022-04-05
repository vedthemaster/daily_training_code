class A{
    public int id;
    public String name;
    void print(){
        System.out.println(id+" from a " +name);

    }
    A(){

        System.out.println("This A's Constructor");
    }
    

} 
class B extends A{
    void print(){
        super.print();
        System.out.println(id+" from b " +name);
    }
    B(){
        System.out.println("This B's Constructor");
    }


}
class C extends  B{
    void print(){
        super.print();
        System.out.println(id+" from c " +name);
    }
    C(int cid, String cname){
        super();
        super.id = cid;
        super.name = cname;
    }
}


public class task1_multilevel_inhe {
    public static void main(String[] args){
        C c1 =  new C(1,"ved");
        c1.print();
    }
    
}
