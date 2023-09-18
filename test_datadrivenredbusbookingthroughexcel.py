from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import openpyexcel
workbook=openpyexcel.load_workbook("..//Projects./datadriven.xlsx")
sheet=workbook.active
totrow=sheet.max_row
totcol=sheet.max_column
mainlist=[]
def test_list():
 for i in range(2,totrow+1):
   datalist=[]
   for j in range(1,totcol+1):
      data=sheet.cell(row=i,column=j).value
      datalist.insert(j,data)
   mainlist.insert(i,datalist)
   print(mainlist)
 return mainlist
@pytest.mark.parametrize("source,destination",test_list())
def test_find(source,destination,get_browser):
    driver=get_browser
    driver.find_element(By.XPATH, "//input[@id='src']").send_keys(source)
    driver.find_element(By.XPATH, "//input[@id='dest']").send_keys(destination)
    time.sleep(2)

