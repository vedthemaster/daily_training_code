package april6;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class facebook_prac2 {
    public static void main(String[] args) {
        
        
        System.setProperty("webdriver.chrome.driver", "C:\\Driver\\chromedriver.exe");
        WebDriver  driver =  new ChromeDriver();
        driver.get("https://www.facebook.com/");

        driver.findElement(By.linkText("Create New Account")).click();
        try{

            Thread.sleep(2000);
        }catch(Exception e){
            System.out.println(e);
        }
        driver.findElement(By.cssSelector("input[name=firstname]")).sendKeys("Ved");
        WebElement lname =  driver.findElement(By.cssSelector("input[name='lastname']"));
        lname.sendKeys("pqr");
        driver.findElement(By.cssSelector("input[name='reg_email__']")).sendKeys("abc@gmail.com");
        driver.findElement(By.cssSelector("input[name='reg_passwd__']")).sendKeys("abc1234");
        driver.findElement(By.cssSelector("input[name='reg_email_confirmation__']")).sendKeys("abc@gmail.com");
        driver.findElement(By.cssSelector("input[name='sex']")).click();


    }
    
}
