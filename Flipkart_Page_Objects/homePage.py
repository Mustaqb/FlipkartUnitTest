from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class HomePage():

    searchFieldXPath = '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input'
    searchButtonXPath = '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button'
    loginModal = '/html/body/div[2]/div/div/button'

    searchProduct = "Asus ROG Zephyrus S Core i7 9th Gen"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def closeLoginModal(self):

        try:
            loginModal = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.loginModal)))

        except NoSuchElementException:
            return

        loginModal.click()

    def setSearchField(self):
        self.driver.find_element_by_xpath(
            self.searchFieldXPath).send_keys(self.searchProduct)

    def clickSearchButton(self):
        self.driver.find_element_by_xpath(self.searchButtonXPath).click()

    def returnDriver(self):
        return self.driver
