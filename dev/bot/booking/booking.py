from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from dev.bot.booking.consts import *
import os
import time


class Booking(webdriver.Chrome):

    def __init__(self,driver_path=r"C:/SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def land_first_page(self):
        self.get("https://www.bbc.com/news/live/world-europe-61124291")
    #

    def get_content(self):
        print("getting content")
        content = self.find_elements(By.TAG_NAME, 'p')
        print(content)
        for block in content:
            print(block.get_attribute('innerText').type + " ")


    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'

        )
        selected_currency_element.click()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def select_place_to_go(self, place):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place)
        choice = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        choice.click()


if __name__ == '__main__':
    b = Booking()
    b.land_first_page()
    b.get_content()