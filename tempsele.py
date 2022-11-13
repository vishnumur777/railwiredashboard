from selenium import webdriver
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import time

chromedriver_autoinstaller.install()

path = "https://tn.railwire.co.in"

# chrome_opt = webdriver.ChromeOptions()
# chrome_opt.add_argument("--headless")
# chrome_opt.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub",options=chrome_opt)
driver = webdriver.Chrome()
driver.get(path)

driver.find_element("id","username").send_keys("tn.varunmurali")

driver.find_element("id","password").send_keys("gurehyhe")

element=driver.find_element("id","captcha_code")
iny = element.get_attribute("outerHTML")

text = ' '.join(BeautifulSoup(iny, "html.parser").stripped_strings)
driver.find_element("id","code").send_keys(text)
driver.find_element("xpath","/html/body/div/div/div[2]/div/div[2]/div/div[1]/form/div[5]/button").click()

driver.get("https://tn.railwire.co.in/subcntl/datausage")
time.sleep(30)
driver.quit()