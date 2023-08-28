#!/opt/anaconda3/bin/python3
import getpass
import smtplib
import time
import os
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver



gmailMsg = "*** APPOINTMENT IS AVAILABLE ***"

print(""" 

 /$$    /$$ /$$                           /$$$$$$              /$$                 /$$                         /$$
| $$   | $$|__/                          /$$__  $$            | $$                | $$                        | $$
| $$   | $$ /$$  /$$$$$$$ /$$$$$$       | $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ | $$
|  $$ / $$/| $$ /$$_____/|____  $$      | $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$| $$
 \  $$ $$/ | $$|  $$$$$$  /$$$$$$$      | $$__  $$| $$  | $$  | $$    | $$  \ $$  | $$    | $$  \ $$| $$  \ $$| $$
  \  $$$/  | $$ \____  $$/$$__  $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$  | $$ /$$| $$  | $$| $$  | $$| $$
   \  $/   | $$ /$$$$$$$/  $$$$$$$      | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/  |  $$$$/|  $$$$$$/|  $$$$$$/| $$
    \_/    |__/|_______/ \_______/      |__/  |__/ \______/    \___/   \______/    \___/   \______/  \______/ |__/

                                            CREATED BY PORAG


DISCLAIMER: Please use this tool reasonably and within the law.
""")



chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("user-data-dir=C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver\\chromeprofile")
chrome_driver = "C:\\Users\\KloverCloud\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)  # driver = webdriver.Chrome()
driver.get('https://ais.usvisa-info.com/en-am/niv/users/sign_in')
time.sleep(3)

# driver = webdriver.Chrome(
#     "C:\\Users\\KloverCloud\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
# driver.get("https://ais.usvisa-info.com/en-am/niv/users/sign_in")
# driver.maximize_window()
# time.sleep(5)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='user_email']")))
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='user_email']").send_keys("martirosyanarax@gmail.com")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='user_password']").send_keys("araksjanjan27")
    time.sleep(1)
    driver.find_element_by_xpath("/html[1]/body[1]/div[5]/main[1]/div[3]/div[1]/div[1]/div[1]/form[1]/div[3]/label[1]/div[1]").click()
    time.sleep(1)

    driver.find_element_by_xpath("/html[1]/body[1]/div[5]/main[1]/div[3]/div[1]/div[1]/div[1]/form[1]/p[1]/input[1]").click()
    time.sleep(5)

    driver.close()

except:
    print("\nERROR: Credentials are incorrect. Please try again...")
