from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
sys.path.append(os.path.abspath(''))
from Flipkart_Page_Objects.ProductDetails import ProductDetailsPage
from Flipkart_Page_Objects.searchedProducts import SearchedProducts
from selenium import webdriver
import HtmlTestRunner
import unittest
from Flipkart_Page_Objects.homePage import HomePage
import time


class Flipkart_Test(unittest.TestCase):

    baseURL = 'https://www.flipkart.com'
    driver = webdriver.Chrome(
        executable_path='webDriver\\chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        cls.wait = WebDriverWait(cls.driver,10)
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()


    def test_searchProduct(self):
        self.home = HomePage(self.driver, self.wait)
        self.home.closeLoginModal()
        self.home.setSearchField()
        self.home.clickSearchButton()
        self.driver = self.home.returnDriver()

    
    def test_searchedProducts(self):
        self.searched = SearchedProducts(self.driver, self.wait)
        productText = self.searched.getProductName()
        self.assertIn(HomePage.searchProduct, productText,
                      "Searched Product not in List")
        self.searched.clickProduct()
        time.sleep(10)
        self.driver = self.searched.returnDriver()

    def test_checkBuyNow(self):
        self.buyNow = ProductDetailsPage(self.driver, self.wait)
        time.sleep(10)
        isBuyNowVisible = self.buyNow.checkBuyNow()
        print('Status of BuyNow button ----->', isBuyNowVisible)
        self.assertTrue(not isBuyNowVisible,
                      "Product is not in stock Currently")
        self.driver = self.buyNow.returnDriver()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='Flipkart_Reports'))

    print(sys.path)
