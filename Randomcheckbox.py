import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get("http://www.tizag.com/htmlT/htmlcheckboxes.php")
driver.maximize_window()
x = driver.find_elements(By.XPATH, '//div[6]//input')
count = len(x)
for i in range(0,4):
 if x[i].is_selected():
    x[i].click()
 else:
     pass
index = random.randrange(1,4,1)
for i in range(0,4):
 random.shuffle(x)
 x[i].click()
