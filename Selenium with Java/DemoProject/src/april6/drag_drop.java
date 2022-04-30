package april6;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

public class drag_drop {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "C:\\Driver\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.get("https://jqueryui.com/droppable/");
        driver.switchTo().frame(0);

        WebElement element = driver.findElement(By.cssSelector("#draggable > p"));
        WebElement element2 = driver.findElement(By.xpath("//*[@id='droppable']"));
        Actions action = new Actions(driver);
        action.dragAndDrop(element, element2).build().perform();

    }
    
}
