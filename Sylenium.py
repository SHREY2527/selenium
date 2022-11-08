import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.action_chains import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager
# from packaging import version
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
# driver.get("https://resumeboss.app/user/login") 
# driver.get("https://resumeboss.app/user/login") 
# driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
#     'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
#     '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    
# email = driver.find_element("id",'identifierId')
# email.send_keys("shrey.kshatrainfotech@gmail.com")
# email.send_keys(Keys.RETURN)

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
# 'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
# '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
# driver.implicitly_wait(15)
  
# loginBox = driver.find_element('xpath','//*[@id ="identifierId"]')
# loginBox.send_keys("shrey.kshatrainfotech@gmail.com")
  
# nextButton = driver.find_elements('xpath','//*[@id ="identifierNext"]')
# nextButton[0].click()
# time.sleep(2)
  
# passWordBox = driver.find_element('xpath',
#     '//*[@id ="password"]/div[1]/div / div[1]/input')
# passWordBox.send_keys("shrey@123")
  
# nextButton = driver.find_elements('xpath','//*[@id ="passwordNext"]')
# nextButton[0].click()

# HDB.click()
driver.get("https://mui5.homeez.com/editor")
HDB = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div')
HDB.click()
time.sleep(2)
Resale= driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div/div/div/div/div/div[2]/div')
Resale.click()
time.sleep(2)
Room_5 = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div/div[4]/div')
Room_5.click()
time.sleep(2)
yes = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[7]/div/div/div/div/div/div/div[1]/div')
yes.click()
time.sleep(2)
Continue = driver.find_element("xpath","/html/body/div/div/div/div/div/div[3]/div/div[2]/div/button")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(Continue).click(Continue).perform()
time.sleep(2)

No_plan = driver.find_element("xpath","/html/body/div/div/div/div/div/div[3]/div/div/div/div[5]/div[2]/div[1]/div/button")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(No_plan).click(No_plan).perform()
time.sleep(2)

image_pro = driver.find_element("xpath","/html/body/div/div/div/div/div/div[3]/div[3]/div/div/div[1]/div/div")
image_pro.click()
time.sleep(2)

proceed = driver.find_element("xpath","/html/body/div/div/div/div/div/div[3]/div[4]/div/button")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(proceed).click(proceed).perform()
time.sleep(2)


claim_ez = driver.find_element("xpath","/html/body/div[3]/div[3]/div/div[4]/button")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(claim_ez).click(claim_ez).perform()
time.sleep(2)

image_2 = driver.find_element("xpath","/html/body/div/div/div/div/div/div[3]/div[2]/div/div/div[2]/div[5]/div/div[1]")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(image_2).click(image_2).perform()
time.sleep(2)


confirm = driver.find_element("xpath","/html/body/div/div/div/div/div/div[3]/div[2]/div/div/div[3]/div/button")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(confirm).click(confirm).perform()
time.sleep(2)

close = driver.find_element("xpath","/html/body/reactour-portal/div[2]/button")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(close).click(close).perform()
time.sleep(2)


Cancle = driver.find_element("xpath","/html/body/div[2]/div[3]/div/h2/div/div[3]/div/button")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(Cancle).click(Cancle).perform()

# upload = driver.find_element("xpath","/html/body/div/div/div/div/div/div[3]/div/div/div/div[5]/div[1]/div/div/div/label/span")
# driver.implicitly_wait(10)
# # time.sleep(1)
# upload.send_keys("C:/Users/ASUS/Downloads/results/141086___141087___142088_1RM_1_ori.png")
# ActionChains(driver).move_to_element(upload).click(upload).perform()
# 
# upload.send_keys(os.getcwd() + "C:/Users/ASUS/Downloads/results/101103___102103___101104___102104___101106___102106_1RM_2_ori")
# upload.send_keys(Keys.RETURN)

# select = driver.find_element("xpath","/html/body/div/div/div/div/div/div[3]/div[3]/button[1]")
# select.click()
# Continue =  driver.find_element("xpath","/html/body/div/div/div/div/div/div[3]/div/div[2]/div/button")
# Continue.click()

# element = WebDriverWait(driver, 10)
# link1 =driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div/div/div/div/div/div[2]/div')
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div/div/div/div/div/div[2]/div"))
        
#     )
#     element.click()
#     element1 = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div/div[4]/div"))
        
#     )
#     element1.click()
    
# except:
#     driver.quit()
# link1.click()
# search = driver.find_element("name", "q")
# driver.find_element('css_selector','#root > div > div > div > div > div.animate__animated.animate__fadeIn.animate__fast.MuiBox-root.css-79elbk > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-item.css-135fl8a > div > button').click()
# search.send_keys("python")
# search.send_keys(Keys.RETURN)
# driver.get("https://mui5.homeez.com/editor")
# link = driver.find_element("link text", "Welcome to Python.org")
#element
# source = driver.find_element_by_id("name")
#action chain object
# action = ActionChains(driver)
# right click operation
# action.context_click(source)


# https://www.google.com/
# print(driver.title)
# driver.quit()


# https://mui5.homeez.com/editor


# HDB-MuiTouchRipple-root css-w0pj6f
# Rescale-MuiTouchRipple-root css-w0pj6f
# image part id-stage-container
# /html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/span[2]
# /html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/span[2]













# from selenium.webdriver.common.keys import 

# driver.maximize_window() 

# from Selenium import webdriver  

# import time  
# from Selenium.webdriver.common.keys import Keys  
# print("sample test case started")  
# driver = webdriver.Chrome()  
# #driver=webdriver.firefox()  
# #driver=webdriver.ie()  
# #maximize the window size  
# driver.maximize_window()  
# #navigate to the url  
# driver.get("https://www.google.com/")  
# #identify the Google search text box and enter the value  
# driver.find_element_by_name("q").send_keys("javatpoint")  
# time.sleep(3)  
# #click on the Google search button  
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
# time.sleep(3)  
# #close the browser  
# driver.close()  
# print("sample test case successfully completed")   


# link = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div')
# link.click()
# # 1 s

# link1 =driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div/div/div/div/div/div[2]/div')
# link1.click()
# 1s
# try:
#     element = webdriverWait(driver,10).until(
#         EC.presence_of_element
    # )