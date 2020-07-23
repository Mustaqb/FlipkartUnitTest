import sys
import os
sys.path.append(os.path.abspath(''))
import time
from Flipkart_Page_Objects.homePage import HomePage
from Flipkart_Page_Objects.searchedProducts import SearchedProducts
from Flipkart_Page_Objects.ProductDetails import ProductDetailsPage
from behave import *
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

@given(u'I Launch Chrome Browser')
def setChrome(context):
    context.driver = webdriver.Chrome(
        executable_path='webDriver\\chromedriver.exe')
    context.wait = WebDriverWait(context.driver, 10)
    


@when(u'I Open Flipkart')
def launchFlipkart(context):
    context.driver.get(context.baseURL)
    context.driver.maximize_window()


@when(u'Enter Product Name in search Field')
def enterProductName(context):
    home = HomePage(context.driver, context.wait)
    home.closeLoginModal()
    home.setSearchField()
    context.driver = home.returnDriver()


@then(u'Click search button')
def searchForProduct(context):
    home = HomePage(context.driver, context.wait)
    home.clickSearchButton()
    context.driver = home.returnDriver()


@given(u'I will be shown list of Products')
def checkListOFProducts(context):
    searched = SearchedProducts(context.driver, context.wait)
    time.sleep(10)
    context.driver = searched.returnDriver()


@when(u'I confirm the product present in obtained list')
def ConfirmSearchedProductPresent(context):
    searched = SearchedProducts(context.driver, context.wait)
    productText = searched.getProductName()
    context.assertIn(HomePage.searchProduct, productText,
                     "Searched Product not in List")
    context.driver = searched.returnDriver()



@then(u'I click on the product')
def selectProduct(context):
    searched = SearchedProducts(context.driver, context.wait)
    searched.clickProduct()
    context.driver = searched.returnDriver()




@given(u'I will be shown product details')
def checkProductDetails(context):
    buyNow = ProductDetailsPage(context.driver, context.wait)
    time.sleep(10)


@when(u'I Check if product is in Stock')
def checkProductInStock(context):
    buyNow = ProductDetailsPage(context.driver, context.wait)
    time.sleep(10)
    isBuyNowVisible = buyNow.checkBuyNow()
    print('Status of BuyNow button ----->')
    context.assertTrue(not isBuyNowVisible,
                       "Product is not in stock Currently")
    context.driver = buyNow.returnDriver()


@then(u'I Close all Browsers')
def closeAllBrowsers(context):
    context.driver.quit()
