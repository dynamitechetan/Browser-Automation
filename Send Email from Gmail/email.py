import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser= webdriver.Chrome()
browser.get("https://mail.google.com")

emailid= browser.find_element_by_id('Email')
emailid.send_keys('Your Email ID')

nextButton= browser.find_element_by_id('next')
nextButton.click()

password = WebDriverWait(browser, 10).until(
   EC.presence_of_element_located((By.ID, 'Passwd')))
password.send_keys('YourPassword')

signInButton = browser.find_element_by_id('signIn')
signInButton.click()

Composeemail= WebDriverWait(browser,10).until(
		EC.presence_of_element_located((By.XPATH, "//div[text()='COMPOSE']")))
Composeemail.click()

mailto = browser.find_element_by_name("to")
mailto.send_keys('Enter Recipient Email ID')

entersubject= WebDriverWait(browser,10)
entersubject= browser.find_element_by_name("subjectbox")
entersubject.send_keys('Auto mail test with Selenium')

mailBody = browser.find_element_by_css_selector("div[aria-label='Message Body']")
mailBody.send_keys('This is an auto generated email. Please Ignore.')
time.sleep(5)

sendmail = WebDriverWait(browser,10)
sendmail = browser.find_element_by_xpath("//div[text()='Send']")
sendmail.click()

logout1 = WebDriverWait(browser,10)
logout1 = browser.find_element_by_class_name('gbii')
logout1.click()

logout2 = browser.find_element_by_id("gb_71")
logout2.click()

time.sleep(3)