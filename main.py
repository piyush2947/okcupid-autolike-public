from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# place the link received on you mail by okcupid in the curly braces below
driver.get("")

actions = ActionChains(driver)
actions.send_keys('2')
while 1:
    actions.perform()

