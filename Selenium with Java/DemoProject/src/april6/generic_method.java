package april6;


import java.security.Key;

import javax.xml.xpath.XPath;
import java.awt.*;
import java.awt.event.KeyEvent;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

public class generic_method {
    public static void main(String[] args)throws InterruptedException,AWTException {
        System.setProperty("webdriver.chrome.driver", "C:\\Driver\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.get("https://courses.letskodeit.com/practice");
        if(driver.findElement(By.xpath("//table[@id='product']"))!= null){
            System.out.println("Element is visible");     
        }
        // Actions action = new Actions(driver);
        // driver.findElement(By.xpath("//input[@id='enabled-example-input']")).sendKeys("Ved");
        //driver.findElement(By.cssSelector("#show-textbox")).click();
        WebElement l=driver.findElement(By.cssSelector("#enabled-example-input"));
        l.sendKeys("xyz");
        System.out.println("Show");
        Thread.sleep(2000);

        Actions act = new Actions(driver);
        driver.findElement(By.cssSelector("#enabled-example-input")).sendKeys(Keys.CONTROL, "a");
        //act.moveToElement(l).doubleClick().build().perform();
        Thread.sleep(2000);
        act.moveToElement(l).contextClick().build().perform();
        Robot robot = new Robot();
        robot.keyPress(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyRelease(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyPress(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyRelease(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyPress(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyRelease(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyPress(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyRelease(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyPress(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyRelease(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        robot.keyPress(KeyEvent.VK_DOWN);
        Thread.sleep(1000);
        //robot.keyRelease(KeyEvent.VK_DOWN);



        robot.keyPress(KeyEvent.VK_ENTER);
        Thread.sleep(1000);
        robot.keyRelease(KeyEvent.VK_ENTER);
        Thread.sleep(1000);



        WebElement a=driver.findElement(By.cssSelector("#displayed-text"));
        a.sendKeys(Keys.chord(Keys.CONTROL,"v"));



        driver.get("https://courses.letskodeit.com");
        driver.findElement(By.xpath("//a[contains(text(),'Sign In')]")).click();
        driver.findElement(By.xpath("//body/div[@id='page']/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]")).sendKeys("samplemail@mail.com");
        Thread.sleep(500);
        driver.findElement(By.id("email")).sendKeys(Keys.TAB);
        Thread.sleep(500);
        driver.findElement(By.xpath("//input[@id='password']")).sendKeys("password");
        driver.findElement(By.xpath("//input[@id='password']")).sendKeys(Keys.TAB);
        // driver.findElement(By.xpath("//input[@id='password']")).sendKeys(Keys.SHIFT,Keys.TAB);
        Thread.sleep(500);
        WebElement ele = driver.findElement(By.xpath("//input[@value='Login']"));
        String ce =  ele.getCssValue("background-color");
        System.out.println(ce);
        driver.findElement(By.xpath("//input[@value='Login']")).sendKeys(Keys.ENTER);
        ele =driver.findElement(By.xpath("//input[@value='Login']"));
        ce =  ele.getCssValue("background-color");
        System.out.println(ce);
        
        driver.findElement(By.id("email")).sendKeys("djfhdfjhdg");
        
        driver.findElement(By.id("email")).sendKeys(Keys.ENTER);
        String eMessage = driver.findElement(By.id("email")).getAttribute("validationMessage");
        System.out.println(eMessage);
        




        

    }
    
}
