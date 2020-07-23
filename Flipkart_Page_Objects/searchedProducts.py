from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchedProducts():

    productXPath = '//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]'


    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    def getProductName(self):

        productDetails = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.productXPath)))

        return productDetails.text

    def clickProduct(self):
        self.driver.find_element_by_xpath(
            self.productXPath).click()
    
    def returnDriver(self):
        return self.driver

