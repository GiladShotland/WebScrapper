import json
from Scrappers.consts import *


def get_content_from_html_elements(elements):
    article = ""
    for element in elements:
        article += element.get_attribute('innerText') + " "
    return article


def get_distinct_elements(arr1, arr2):
    ans = [x for x in arr1 if x not in arr2]
    return ans
