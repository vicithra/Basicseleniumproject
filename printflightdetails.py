import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get("https://www.makemytrip.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,'//div[@data-cy="flightSW"]/div[1]/ul/li[2]').click()
actions = ActionChains(driver)
From = driver.find_element(By.ID,'fromCity').send_keys("New York")
time.sleep(2)
opt1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/ul/li[1]/div/div[1]/p[1]')
actions.click(opt1).perform()
To = driver.find_element(By.ID, 'toCity').send_keys("London")
time.sleep(2)
opt2 = driver.find_element(By.XPATH,
                           '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div/ul/li[1]')
actions.click(opt2).perform()
frdate = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[6]')
actions.click(frdate).perform()
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[5]').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[2]/p/a').click()
time.sleep(9)
flights = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div')
print(len(flights))
d=driver.find_elements(By.XPATH,"//p[contains(@class,'airlineName')]")
p=driver.find_elements(By.XPATH,"//div[@class='priceSection']/div/div/p")
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/button').click()
for i in range(0,len(flights)):
    print(d[i].text,p[i].text)

