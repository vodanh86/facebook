# cai dat va chay script selenium : https://selenium-python.readthedocs.io/
import time
import traceback 
import user
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import pickle

def scroll_down(driver):
    """A method for scrolling the page."""
    sleep_time = 4
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")
    count = 0
    while True:
        '''count = count + 1
        if count > 3:
            break'''
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(sleep_time)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            for i in range(100):
                print(i)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(sleep_time)
                new_height = driver.execute_script("return document.body.scrollHeight")
                
                if new_height != last_height:
                    break
            if new_height == last_height:
                break
        last_height = new_height

messages = open("message.txt").readlines()

options = FirefoxOptions()
#options.add_argument("--headless")

desired_capability = webdriver.DesiredCapabilities.FIREFOX
desired_capability['proxy']={
    "proxyType":"manual",
    "httpProxy": "94.140.228.197:81",
}        

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
driver = webdriver.Firefox(options=options, firefox_profile=firefox_profile, capabilities=desired_capability) 

driver.get("https://facebook.com")

elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys(user.fb_user)

elem = driver.find_element_by_name("pass")
elem.clear()
elem.send_keys(user.fb_pass)

elem.send_keys(Keys.RETURN)

try:
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/groups/"]'))
    )
    print("Headless Firefox Initialized")
except WebDriverException:
    print("abcd")


driver.quit()       
