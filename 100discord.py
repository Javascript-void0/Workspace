from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://discord.com/app')
# driver.find_element_by_xpath('.//*[@id="app-mount"]/div[2]/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys('atcdiscord@gmail.com')
# driver.find_element_by_xpath('.//*[@id="app-mount"]/div[2]/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys('LOL')
d = driver.find_elements_by_xpath('.//*[@id="app-mount"]/div[2]/div/div/div/div')
print(d)