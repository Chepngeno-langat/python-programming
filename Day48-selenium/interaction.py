from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/karen/Documents/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("")
# num_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(num_of_articles.text)
#
# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# #all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)