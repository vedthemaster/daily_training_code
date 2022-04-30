package april6;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.Select;

import java.util.*;

public class letscodeit_tasks {

    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Driver\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.get("https://courses.letskodeit.com/practice");

        WebElement sText = driver.findElement(By.xpath("//legend[contains(text(),'Radio Button Example')]"));
        String text = sText.getText();

        Actions action = new Actions(driver);
        WebElement element = driver.findElement(By.id("mousehover"));
        action.moveToElement(element).perform();
        Thread.sleep(1000);
        driver.findElement(By.xpath("//a[contains(text(),'Top')]")).click();
        Thread.sleep(1000);
        action.moveToElement(element).perform();
        driver.findElement(By.xpath("//a[contains(text(),'Reload')]")).click();

        for(int j=1; j<4; j++)
        {
        for(int i=2;i<5; i++)
        {
        String data = driver.findElement(By.xpath("//*[@id=\"product\"]/tbody/tr["+i+"]/td["+j+"]")).getText();
        System.out.println("Data : " + data+ " Row: " +(i-1) + " Column: " +j);
        }
        }
        System.out.println(text);
        List<WebElement> rCount = driver.findElements(By.xpath("//input[@name='cars']"));
        int count = rCount.size();
        System.out.println(count);
        try {
            driver.findElement(By.cssSelector("input[name='cars']")).click();
            Thread.sleep(1000);
            driver.findElement(By.cssSelector("input[value='benz']")).click();
            Thread.sleep(1000);
            driver.findElement(By.cssSelector("input[value='honda']")).click();
            Thread.sleep(1000);
        } catch (Exception e) {
        }

        Select s = new Select(driver.findElement(By.cssSelector("select[name=cars]")));
        System.out.println("Check Here"+ s.isMultiple());
        s.selectByVisibleText("Honda");
        
        try {
            
            WebElement s3 = driver.findElement(By.cssSelector("#multi-select-example-div > fieldset > legend"));
            
            String st2 = s3.getText();
            System.out.println("Text is : " + st2);
            
            driver.findElement(By.cssSelector("#multiple-select-example > option:nth-child(1)")).click();
            Thread.sleep(200);
            driver.findElement(By.cssSelector("#multiple-select-example > option:nth-child(2)")).click();
            Thread.sleep(200);
            driver.findElement(By.cssSelector("#multiple-select-example > option:nth-child(3)")).click();
            
            Thread.sleep(500);
        } catch (Exception e) { }
        
        Select mul= new Select(driver.findElement(By.id("multiple-select-example")));
        System.out.println("Check Here"+ mul .isMultiple());
        if(mul.isMultiple())
        {
        String ob2 = driver.findElement(By.cssSelector("#multi-select-example-div > fieldset > legend")).getText();
        System.out.println(ob2);

        driver.findElement(By.cssSelector("#multiple-select-example > option:nth-child(1)")).click();
        Thread.sleep(200);

        driver.findElement(By.cssSelector("#multiple-select-example > option:nth-child(2)")).click();
        Thread.sleep(200);

        driver.findElement(By.cssSelector("#multiple-select-example > option:nth-child(3)")).click();
        }
        Thread.sleep(500);
        driver.findElement(By.xpath("//input[@id ='bmwcheck']")).click();

        driver.findElement(By.xpath("//body/div[@id='page']/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/fieldset[1]/input[1]")).sendKeys("Ved");
        driver.findElement(By.xpath("//input[@id='alertbtn']")).click();
        Thread.sleep(1000);
        driver.switchTo().alert().accept();

        driver.findElement(By.id("openwindow")).click();
        Thread.sleep(2000);
        String winHandleBefore = driver.getWindowHandle();
        for(String winHandle : driver.getWindowHandles())
        {
        driver.switchTo().window(winHandle);
        System.out.println(driver.getTitle());
        }
        Thread.sleep(2000);
        driver.switchTo().window(winHandleBefore);
        Thread.sleep(2000);
        System.out.println(driver.getTitle());
        Thread.sleep(2000);
        driver.quit();
    }   

}
