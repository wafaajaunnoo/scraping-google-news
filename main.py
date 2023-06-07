from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

def scrape_google_news(query)
  url=f""
  driver = webdriver.Chrome()
  driver.get(url)
  
  scraped_data = []
  
  while true:
    #allow page-loading time
    time.sleep(2)
    titles = driver.find_elements(By.CSS_SELECTOR, "")
    
