package april6;
import org.openqa.selenium.chrome.*;
import org.openqa.selenium.WebDriver;

public class Demo01 {
    public static void main(String[] args) {
        WebDriver  driver = new ChromeDriver();
        driver.get("http://demowebshop.tricentis.com/");
        System.out.println(driver.getTitle());
    }
}
