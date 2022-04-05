from selenium import webdriver

driver = webdriver.Chrome(
    executable_path='C:\\Users\\vedpa\\OneDrive\\Desktop\\Drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://sites.google.com/ganpatuniversity.ac.in/ftt2022/shift-ii/track-i/feedback?authuser=0")

driver.find_element(by= By.CLASS_NAME, value="whsOnd zHQkBf").send_keys("vedpatel3395@gmail.com")