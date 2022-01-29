from selenium import webdriver
import requests
from random import randint
from time import sleep

def random():
	get_name = requests.get('https://random-data-api.com/api/name/random_name')
	get_word = requests.get('https://random-word-form.herokuapp.com/random/noun')
	n = randint(1, 3)
	if n == 1:
		bd = randint(101, 1230)
		name = get_name.json()
		word = get_word.json()
		email = name['two_word_name'].replace(' ', '.') + str(bd) + '@gmail.com'
		password = word[0] + str(bd)
		return email, password
	elif n == 2:
		bd = randint(101, 1230)
		name = get_name.json()
		email = name['name'].replace(' ', '') + '@gmail.com'
		password = name['two_word_name'].replace(' ', '') + str(bd)
		return email, password
	elif n == 3:
		bd = randint(101, 1230)
		name = get_name.json()
		email = name['first_name'].replace(' ', '') + str(bd) + '@outlook.com'
		password = str(bd) + name['name'].replace(' ', '')
		return email, password

for i in range(100):
	email, password = random()
	print('Email: ' + email)
	print('Password: ' + password)

	driver = webdriver.Chrome()
	driver.get('https://minehut-partnership.herokuapp.com/')
	sleep(1)
	emailInput = driver.find_element_by_xpath('//*[@id="1-email"]')
	emailInput.send_keys(email)
	passwordInput = driver.find_element_by_xpath('//*[@id="1-password"]')
	passwordInput.send_keys(password)
	submit = driver.find_element_by_xpath('//*[@id="auth0-main"]/div/div/div/button')
	submit.click()
	sleep(1)
	driver.close()