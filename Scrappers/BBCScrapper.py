from selenium.webdriver.common.by import By
from Scrappers.NewsScrapper import *
from ProjectUtils.FilesHandler import *
from ProjectUtils.ArticleBuilder import *


class BBCScrapper(NewsScrapper):

    def __init__(self, url=BBC_PATH, driver_path=CHROME_DRIVER_PATH, teardown=False):
        super(BBCScrapper, self).__init__(url,BBC_ARTICLES_LIST_JSON, BBC_ARTICLES_CONTENT_JSON,
                                          driver_path=CHROME_DRIVER_PATH, teardown=False)
        self.land_first_page()

    def download_articles(self):
        """
        extracting the content and saving it
        :return: articles
        """
        articles,urls = self.extract_content()
        self.save_content(articles)
        return articles, urls

    def extract_content(self):
        """
        pulling links for the articles in the main page
         than taking only the ones we didn't downloaded yet

        :return: articles,urls
        """
        self.pull_links()
        urls = self.get_relevant_content()
        articles = self.file_handler.get_from_json(BBC_ARTICLES_CONTENT_JSON)
        article_builder = ArticleBuilder()
        for url in urls:
            genre = self.get_genre_from_url(url)
            # this genre is video article
            if genre == 'reel':
                continue
            html_elements = self.get_html_elemnts_frm_article(url)
            article = article_builder.get_article_from_html_elements(html_elements)
            articles[url] = article

        self.article_links = urls + self.file_handler.get_from_json(self.articles_list_file)
        return articles, urls

    def get_html_elemnts_frm_article(self, url):
        """
        getting the elements of paragraphs
        :param url: url of the article
        :return: html elements of pargraphs in the article
        """
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
        """
        getting the elements with links to articles and getting the links
        :return:
        """
        article_links = []
        for href in self.pull_hrefs():
            article_link = href.get_attribute('href').strip()
            article_links.append(article_link)
        self.article_links = article_links

    def pull_hrefs(self):
        """
        pulling hrefs
        :return: hrefs of urls for articles
        """
        article_links = []
        hrefs = self.find_elements(By.CSS_SELECTOR, 'a[class="block-link__overlay-link"]')
        return hrefs

