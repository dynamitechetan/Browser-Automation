import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChalkpadLogin(unittest.TestCase):

    def setUp(self):
        self.driver =webdriver.Chrome("D:\chromedriver\chromedriver")

    def test_login(self):
        driver = self.driver
       
        usr = "rollNumberPleaseReplace"
        pwd = "PASSWORD"
        driver = webdriver.Chrome("D:\chromedriver\chromedriver")
        # or you can use Chrome(executable_path="/usr/bin/chromedriver")
        driver.get("http://punjab.chitkara.edu.in//Interface/index.php")
        assert "Chalkpad" in driver.title
        elem = driver.find_element_by_id("username")
        elem.send_keys(usr)
        elem = driver.find_element_by_id("password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        self.assertTrue(driver.find_element_by_link_text("Logout"),"Logout link")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
