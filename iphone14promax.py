import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.find_element(By.ID,'twotabsearchtextbox').send_keys("iphone 14 pro max")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='left-pane-results-container']/div[1]").click()
x=driver.find_element(By.XPATH,"//img[@data-image-index='1']")
m=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').text
print(m)
x.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.execute_script("window.scrollTo(0,750)")
driver.find_element(By.XPATH,"//input[@id='add-to-cart-button']").click()
time.sleep(2)
y=driver.find_element(By.XPATH,"//input[@aria-labelledby='attach-sidesheet-view-cart-button-announce']")
time.sleep(3)
y.click()
l=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[2]/ul/li[1]/span/a/span[1]/span/span[2]').text
print(l)
assert m==l,"same product"