from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

class ProductDetailsPage():

    buyNowButtonXPath = '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button'

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def checkBuyNow(self):

        time.sleep(5)


        try:
            buyNow = self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.buyNowButtonXPath)))

        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

        return buyNow.is_displayed()

    def returnDriver(self):
        return self.driver
        
