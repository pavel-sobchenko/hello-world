import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo.magentocommerce.com/")

    def test_search_by_category(self):
        self.search_button = self.driver.find_element_by_xpath("//a[@title='Search']")
        self.search_button.click()

        self.search_field = self.driver.find_element_by_id("edit-keys")
        self.search_field.clear()

        self.search_field.send_keys("phone")
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//li[@class='gss-result']")
        self.assertEquals(20, len(products))

    def test_search_by_name(self):
        self.search_button = self.driver.find_element_by_xpath("//a[@title='Search']")
        self.search_button.click()

        self.search_field = self.driver.find_element_by_id("edit-keys")
        self.search_field.clear()

        self.search_field.send_keys("salt-sneaker")
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//li[@class='gss-search']")
        self.assertEquals(0, len(products))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)