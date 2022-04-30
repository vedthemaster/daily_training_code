package april6;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class demo1 {
    public static void main(String[] args) {
      
            System.setProperty("webdriver.chrome.driver", "C:\\Driver\\chromedriver.exe");
            WebDriver  driver =  new ChromeDriver();
            // driver.get("http://demowebshop.tricentis.com/");
            driver.navigate().to("http://demowebshop.tricentis.com/");;
            System.out.println(driver.getTitle()); 
    }
    
}
