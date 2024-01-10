from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from bs4 import BeautifulSoup 

service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.nirmalbang.com/nb-research/equity-technical-intraday-tips-and-calls.aspx")
input_element = driver.find_element("xpath",'//*[@id="rch_txtmobile"]')
input_element.send_keys('8828420553')
# Print the page title (to verify successful navigation)
link_element = driver.find_element("id",'checkresearchmobile')
link_element.click()
sleep(15)
html = driver.page_source 
  
# this renders the JS code and stores all 
# of the information in static HTML code. 
  
# Now, we could simply apply bs4 to html variable 
soup = BeautifulSoup(html, "html.parser") 
print(soup.prettify())
all_divs = soup.find('tbody', {'id' : 'technicalcallcontent'}) 
print(all_divs)
tds = all_divs.find_all('td') 
print(tds)
count = 0
for td in tds : 
    print(td.text) 
    count = count + 1
    if(count == 10) : 
        break
print(driver.title)
sleep(10)
driver.quit()