from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://minecraftservers.org/vote/443456?')
username = driver.find_element_by_xpath('//*[@id="field-container"]/form/ul/li/input')
username.send_keys('Javascript_void0')
print('Now Complete the Captcha :D')