from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

# Step 1) Open Firefox
driver = webdriver.Chrome()
# Step 2) Navigate to Facebook
driver.get("https://www.learnvern.com/auth/login")
time.sleep(2)
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = driver.find_element("id","email")
username.send_keys("Rajni2955@gmail.com")
password = driver.find_element("id","password")
password.send_keys("injar2121tayalbn")
submit= driver.find_element("id","loginSubmit")
# Step 4) Click Login
submit.click()
wait = WebDriverWait(driver, 5)
page_title=driver.title
time.sleep(2)
search=driver.find_element("id","search-megamenu-input")
search.send_keys("C++")
search.send_keys(Keys.RETURN)

time.sleep(2)
driver.close()