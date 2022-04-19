from selenium import webdriver
from ProjectUtils.Consts import *

import os


class Scrapper(webdriver.Chrome):
    """
    Scrapper Class for initializing a scrapper and landing the first page
    """
    def __init__(self, url, driver_path=CHROME_DRIVER_PATH, teardown=False):
        self.url = url
        self.driver_path = driver_path
        self.teardown = teardown
        super(Scrapper, self).__init__(r"C:/SeleniumDrivers/chromedriver.exe")
        self.implicitly_wait(10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(self.url)





