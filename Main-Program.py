import openpyxl
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from SeleniumDemo import UtilsFunctions  # Importing UtilsFunctions module to this module


serv_obj=Service("C:\Se\chromedriver.exe")
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")     # to disable alerts
driver=webdriver.Chrome(service=serv_obj, options=ops)
driver.implicitly_wait(1)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
file="C:\\Users\\Admin\\Downloads\\Test-File.xlsx"
rows=UtilsFunctions.getRowCount(file,"Sheet1")  #Calling the function inside the module

# Getting the function from the imported Module and passing arguments
for r in range(2,rows+1): # Starting from second row
    princ = UtilsFunctions.readData(file,"Sheet1",r,1) # Passing 3 arguments here
    rateOfInterest = UtilsFunctions.readData(file,"Sheet1",r,2)
    per1 = UtilsFunctions.readData(file,"Sheet1",r,3)
    per2 = UtilsFunctions.readData(file,"Sheet1",r,4)
    fre = UtilsFunctions.readData(file,"Sheet1",r,5)
    exp_mvalue = UtilsFunctions.readData(file,"Sheet1",r,6)  # It is in string format

    # Passing data to the application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateOfInterest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

    perioddrp=Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))  # Period Drop down
    perioddrp.select_by_visible_text(per2) # Selecting from the dropdown

    frequencydrp=Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))  # Frequency drop down
    frequencydrp.select_by_visible_text(fre)
    #driver.find_element(By.XPATH, "//*[@id='wzrk-confirm']").click()  # clicking yes in the popup button
    driver.find_element(By.XPATH, "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click() # Calculate button

    act_mvalue=driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text # We captured the result we got by alterting Xpath and copied it. (Because the value is dynamically changing).

    #Validation
    if float(exp_mvalue)==float(act_mvalue):  # we are converting the values into a float and comparing
        print("test passed")
        UtilsFunctions.writeData(file,"Sheet1",r,8,"Passed")
        UtilsFunctions.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        UtilsFunctions.writeData(file,"Sheet1",r,8,"Failed")
        UtilsFunctions.fillRedColor(file,"Sheet1", r,8)
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()  # To click on the clear button in order to clear the data before the loop is repeated





