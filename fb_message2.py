# cai dat va chay script selenium : https://selenium-python.readthedocs.io/

import user
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

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
