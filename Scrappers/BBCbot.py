from selenium.webdriver.common.by import By
from Scrappers.consts import *
from Bot import *
from NewsBot import *
from Scrappers.consts import *
from json_utils import *
from utils import *


class BBCScrapper(NewsScrapper):

    def __init__(self, url=BBC_PATH, driver_path=CHROME_DRIVER_PATH, teardown=False):
        super(BBCScrapper, self).__init__(url,BBC_ARTICLES_LIST_JSON, BBC_ARTICLES_CONTENT_JSON,
                                          driver_path=CHROME_DRIVER_PATH, teardown=False)
        self.land_first_page()


    def download_articles(self):
        self.extract_content()

    def extract_content(self):
        self.pull_links()
        urls = self.get_relevant_content()
        articles = get_from_json(BBC_ARTICLES_CONTENT_JSON)
        for url in urls:
            genre = self.get_genre_from_url(url)
            if genre == 'reel':
                continue
            html_elements = self.get_html_elemnts_frm_article(url)
            article = get_content_from_html_elements(html_elements)
            articles[url] = article

        self.article_links = urls + get_from_json(self.articles_list_file)
        self.save_content(articles)

        return articles, urls

    def get_html_elemnts_frm_article(self, url):
        self.get(url)
        return self.find_elements(By.TAG_NAME, 'p')

    def get_genre_from_url(self,url):
        """

        :param url:
        :return: Genre of the article

        """
        # url form is http://www.bbc.com/genre/....
        return url.split('/')[3]



    def pull_links(self):
        self.article_links = self.pull_links_from_href()

    def pull_links_from_href(self):
        article_links = []
        hrefs = self.find_elements(By.CSS_SELECTOR, 'a[class="block-link__overlay-link"]')
        for href in hrefs:
            article_link = href.get_attribute('href').strip()
            article_links.append(article_link)

        return article_links


if __name__ == '__main__':
    b = BBCScrapper(teardown=True)
    b.download_articles()
    print(b.articles_summary()[0])
    print(b.sentiment_analysis()[0])
