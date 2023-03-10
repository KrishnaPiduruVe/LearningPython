from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class TestSearchDemo():
    @pytest.fixture(scope='module')
    def setUptearDownClass(self):
        global driver
        driver = webdriver.Firefox()

    @pytest.fixture()
    def setUptearDownMethod(self):
        driver.get("https://www.linkedin.com/")
        driver.maximize_window()
        yield
        time.sleep(5)
        driver.close()

    def test_linkedin_search(self, setUptearDownClass, setUptearDownMethod):
        print("test_linkedin_search")
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
