from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path=r"/root/Test/chromedriver",chrome_options=chrome_options)
driver.get("https://www.digitalocean.com/")
title = driver.title
driver.quit()
print(title)
