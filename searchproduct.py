import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://demo.magentocommerce.com/")

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

        self.search_field.send_keys("salt shaker")
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//li[@class='gss-result']")
        self.assertEquals(1, len(products))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=3)
