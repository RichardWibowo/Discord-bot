from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def auth101(test):
    if(auth == 1) :
        username = 46112820
        password = "Dkx3.wkDWe8pfK9"
        print("hi, richard")
    
def Start() :    
    #open ilearn
    PATH = "D:\Key Log\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://ilearn.mq.edu.au/login/index.php")

            #pass login
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear
    password.clear
    x = username 
    y = password
    username.send_keys(x)
    password.send_keys(y)
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

def Class_Online() :
    #enter class WCOM1010
    driver.get("https://ilearn.mq.edu.au/course/view.php?id=44410")
   
