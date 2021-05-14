from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://discord.com/app')
sleep(10)
new_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[4]/div/div[2]/div/svg').click()