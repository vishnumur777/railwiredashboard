import pandas as pd

from selenium import webdriver
#import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager

import time
import os
import codecs
from bs4 import BeautifulSoup

path = "https://tn.railwire.co.in"

chrome_opt = Options()

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

driver.get("https://tn.railwire.co.in/subcntl")

ne = os.path.join("/home/VARUN/Documents/cnminiproject","railhome.html")

f = codecs.open(ne,"w","utf-8")

h = driver.page_source

f.write(h)

driver.quit()

html = open("/home/VARUN/Documents/cnminiproject/railhome.html","r",encoding="utf-8")

store = html.read()

text = ' '.join(BeautifulSoup(store, "html.parser").stripped_strings)

te = list(text.split())

p = []
for i in te:
    if(i=="Username"):
        p.append(te[te.index(i)+2])
    if(i=="Email"):
        p.append(te[te.index(i)+3])
    if(i=="Fee:"):
        p.append(te[te.index(i)+2])
    if(i=="Name:"):
        p.append(te[te.index(i)+1] + " " +te[te.index(i)+2])
    if(i=="Status:"):
        p.append(te[te.index(i)+1])
    if(i=="Subscriberid"):
        p.append(te[te.index(i)+2])
    if(i=="Expiry"):
        p.append(te[te.index(i)+2])
    if(i=="Last"):
        p.append(te[te.index(i)+3])

details = ["Username","Email","Price","Plan Name","Status","Subscriber Id","Expiry","Last renewal"]

userdata = pd.DataFrame(zip(details,p),columns = ["Details","Data"])

userdata.to_csv("userdata.csv")

