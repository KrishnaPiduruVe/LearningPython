'''
write a python test script to test google search functionality by using selinum unit testing  ?

What is Selenium ?
    Funtional testing automation tool

We have to install selenium package 

pip install selenium ==> Install pip

pip install --upgrade pip 
    ==> upgrade pip 
    ===> If ERROR: Could not install packages due to an EnvironmentError: [WinError 5] Access is denied: 'C:\\Users\\venka\\AppData\\Local\\Temp\\pip-uninstall-gdvzc6ou\\pip.exe'
        Consider using the `--user` option or check the permissions ==>
pip install --upgrade pip --user

selenium : package 
webdriver : module

webdriver module contains several classes and functions to test functionality of the web application

Launch browser :
    browser driver must be required to launch our browser
    seleniumhq.org

Browser interaction and navigation of web pages:

driver.get(url) ==> to open specified url
driver.maximize_window()
driver.title
driver.current_url
driver.refresh() or  driver.get(driver.current_url)
driver.back() ===> goes one step backward in the browser history
driver.forward ===> goes one step forward in the browser history
driver.close()  ===> close current window
driver.quit() ===> close associated windows  


driver.find_element("id",'id')
driver.find_element("name",'name')
driver.find_element("text",'txt')
driver.find_element("css selector",'css')

expected one of `css selector`, 
`link text`, `partial link text`, `tag name`, `xpath`


'''

from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By


class SearchDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Firefox()

    def setUp(self):
        driver.get("https://www.linkedin.com/")
        driver.maximize_window()

    def test_method1(self):
        print("test_method1")
        driver.find_element("name", "session_key").send_keys(
            "krishnapiduruve@outlook.com")
        driver.find_element("name", "session_password").send_keys(
            "Krishna*123")
        driver.find_element("css selector", "button.btn-primary").click()

        '''
        try:
            driver.find_element("css selector", ".primary-action-new").click()
        except Exception as ex:
            print(ex)
        '''
        time.sleep(30)
        driver.find_element(By.LINK_TEXT, "Jobs").click()

        driver.implicitly_wait(20)
        driver.find_element(
            By.CSS_SELECTOR, "input.jobs-search-box__keyboard-text-input:nth-child(4)").send_keys("Apache Spark")

    def tearDown(self):
        time.sleep(5)
        # driver.close()

    '''
    driver.get("https://www.linkedin.com/in/venkat-piduru-97866b68/")      
    driver.refresh()
    print("Title : ", driver.title)
    print("Current Page Url : ", driver.current_url)
    driver.get("http://facebook.com/")
    print("Current Page Url : ", driver.current_url)
    driver.back()
    print("back Current Page Url : ", driver.current_url)
    time.sleep(5)
    driver.forward()
    print("after Current Page Url : ", driver.current_url)
    driver.close()
    '''


unittest.main()
