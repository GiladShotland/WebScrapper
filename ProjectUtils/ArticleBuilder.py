import json
from ProjectUtils.Consts import *
from selenium.webdriver.common.by import By

class ArticleBuilder:


    def get_article_from_html_elements(self, elements):
        """
        getting the text from the html elements
        :return: txt of the article
        """
        article = ""
        for element in elements:
            article += element.get_attribute('innerText') + " "
        return article





