from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from bs4 import BeautifulSoup 
import csv

service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.nirmalbang.com/nb-research/equity-technical-intraday-tips-and-calls.aspx")
input_element = driver.find_element("xpath",'//*[@id="rch_txtmobile"]')
input_element.send_keys('8828420553')
link_element = driver.find_element("id",'checkresearchmobile')
link_element.click()
sleep(15)
html = driver.page_source 
  

soup = BeautifulSoup(html, "html.parser") 
# print(soup.prettify())
all_divs = soup.find('tbody', {'id' : 'technicalcallcontent'}) 
# print(all_divs)
trs = all_divs.find_all('tr') 
# print(tds)
count = 0
tips=[]
for tr in trs : 
    tds = tr.find_all('td')
    td_texts = [td.text for td in tds]
    print(td_texts)
    print()
    tips.append(td_texts)
    
with open('tips.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(tips)
# print(tips)
sleep(10)
driver.quit()