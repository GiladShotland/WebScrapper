from selenium import webdriver
from Scrappers.consts import *

import os


class Scrapper(webdriver.Chrome):
    """
    Scrapper Class for initializing a scrapper and landing the first page
    """
    def __init__(self, url, driver_path=CHROME_DRIVER_PATH, teardown=False):
        self.url = url
        self.driver_path = driver_path
        self.teardown = teardown
        self.set_env()
        super(Scrapper, self).__init__()
        self.implicitly_wait(10)

    def set_env(self):
        os.environ['PATH'] += self.driver_path

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(self.url)





