public class Constructor_imp {
    private int stuID ;
    private String stuName;
    private int stuAge;
    Constructor_imp(){
        stuID = 12;
        stuName = "Kushang";
        stuAge = 21;
        
    }
    public void setStuName(){
        this.stuName = stuName;

    }
    public String getStuName(){
        return stuName;
    }
    public void setStuID(){
        this.stuID = stuID;

    }
    public int getStuID(){
        return stuID;
    }
    public void setStuAge(){
        this.stuID = stuID;

    }
    public int getStuAge(){
        return stuAge;
    }
    Constructor_imp(int sID,String sName,int sAge){
        stuID = sID;
        stuName = sName;
        stuAge = sAge;
        
    }
    void display(){
        System.out.println(stuID+ " "+ stuName + " "+stuAge );
    }

    public static void main(String[] args){
        Constructor_imp stu1 = new Constructor_imp();
        Constructor_imp stu2 = new Constructor_imp(25,"Ved",21);
        stu1.display();
        stu2.display();
    }
}
