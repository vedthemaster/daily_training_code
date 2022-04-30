package april6;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class facebook {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "C:\\Driver\\chromedriver.exe");
        WebDriver  driver =  new ChromeDriver();
        driver.get("https://www.facebook.com/");
        // By ID
        driver.findElement(By.id("email")).sendKeys("test");
        driver.findElement(By.id("pass")).sendKeys("password");

        // driver.findElement(By.name("login")).click();
        // driver.findElement(By.linkText("Forgotten password?")).click();
        driver.findElement(By.xpath("//a[contains(text(),'Forgotten password?')]")).click();

        
    }
    
}
