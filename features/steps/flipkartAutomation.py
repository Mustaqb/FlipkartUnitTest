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
    context.baseURL = 'https://www.flipkart.com'
    context.wait = WebDriverWait(context.driver, 10)
    

@when(u'I Open Flipkart')
def launchFlipkart(context):
    context.driver.get(context.baseURL)
    context.driver.maximize_window()


@when(u'Enter Product Name in search Field')
def enterProductName(context):
    context.home = HomePage(context.driver, context.wait)
    context.home.closeLoginModal()
    context.home.setSearchField()
    context.driver = context.home.returnDriver()


@when(u'Click search button')
def searchForProduct(context):
    context.home.clickSearchButton()
    context.driver = context.home.returnDriver()


@when(u'I will be shown list of Products')
def checkListOFProducts(context):
    context.searched = SearchedProducts(context.driver, context.wait)
    time.sleep(10)
    context.driver = context.searched.returnDriver()


@when(u'I confirm the product present in obtained list')
def ConfirmSearchedProductPresent(context):
    productText = context.searched.getProductName()
    # assert_that(context.HomePage.searchProduct, equal_to(productText))
    # assert context.home.searchProduct is productText
    context.driver = context.searched.returnDriver()


@when(u'I click on the product')
def selectProduct(context):
    context.searched.clickProduct()
    context.driver = context.searched.returnDriver()


@when(u'I will be shown product details')
def checkProductDetails(context):
    context.buyNow = ProductDetailsPage(context.driver, context.wait)
    time.sleep(10)


@when(u'I Check if product is in Stock')
def checkProductInStock(context):
    time.sleep(10)
    isBuyNowVisible = context.buyNow.checkBuyNow()
    print('Status of BuyNow button ----->', isBuyNowVisible)
    context.driver = context.buyNow.returnDriver()


@then(u'I Close all Browsers')
def closeAllBrowsers(context):
    context.driver.quit()
