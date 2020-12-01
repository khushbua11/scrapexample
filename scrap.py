from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

def get_source(html):
    soup = BeautifulSoup(html,'html.parser')
    return soup

#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
options = Options()
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--silent")
browser = webdriver.Chrome('/var/www/Scrapping/PythonScrap/chromedriver', options=options)

# to maximize the browser window
# browser.maximize_window()

#get method to launch the URL
browser.get("http://bank-code.net/country/FRANCE-%28FR%29/")

time.sleep(5)

while True:
	soup = get_source(browser.page_source)
	table = soup.find(name='table', attrs={'class':'table-bordered'})	
	rows = table.tbody.findAll('tr')
	try:
		for row in rows:
			tds = row.findAll('td')
			for td in tds:
				data = td.text
				print(data)
		link = browser.find_element_by_link_text(">").click()
	except:
		pass

#to close the previous tabs of browser
browser.quit()

#to refresh the browser
# browser.refresh()

#to close the browser
# browser.close()
