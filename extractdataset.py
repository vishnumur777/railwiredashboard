from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import codecs
import pandas as pd
from bs4 import BeautifulSoup


path = "https://tn.railwire.co.in"

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("--headless")
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub",options=chrome_opt)

driver.get(path)

driver.find_element("id","username").send_keys("tn.varunmurali")

driver.find_element("id","password").send_keys("gurehyhe")
element=driver.find_element("id","captcha_code")
iny = element.get_attribute("outerHTML")
text = ' '.join(BeautifulSoup(iny, "html.parser").stripped_strings)
driver.find_element("id","code").send_keys(text)

driver.find_element("xpath","/html/body/div/div/div[2]/div/div[2]/div/div[1]/form/div[5]/button").click()

driver.get("https://tn.railwire.co.in/subcntl/datausage")

ne = os.path.join("/home/VARUN/Documents/cnminiproject","Railwire Billing.html")

f = codecs.open(ne,"w","utf-8")

h = driver.page_source

f.write(h)

driver.quit()

data = pd.read_html("Railwire Billing.html")

data[0].to_csv("RailwireBilling.csv")
