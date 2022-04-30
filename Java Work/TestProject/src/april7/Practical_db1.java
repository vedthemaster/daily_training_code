package april7;
import java.sql.*;

public class Practical_db1 {
    public static void main(String[] args) throws SQLException, ClassNotFoundException {
        Connection conn;
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn =  DriverManager.getConnection("jdbc:mysql://localhost:3306/demodb","root","1234");
            System.out.println("Connected Successfully");
        }catch (ClassNotFoundException e){
            System.out.println(e);

        }
    }
    
}
