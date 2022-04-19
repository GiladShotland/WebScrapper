from Scrappers.Scrapper import *
from ProjectUtils.Consts import *
import json
from ProjectUtils.FilesHandler import *
from ProjectUtils.ArticleBuilder import *


class NewsScrapper(Scrapper):
    """
    News Scrapper Class -
    """

    def __init__(self, url, articles_list_file, articles_content_file, driver_path=CHROME_DRIVER_PATH, teardown=False):
        """
        initializing file handler and articles list and content
        """
        self.file_handler = FilesHandler()
        self.file_handler.initialize_news_files(articles_list_file, articles_content_file)
        super(NewsScrapper, self).__init__(url, driver_path, teardown)
        self.articles_list_file = articles_list_file
        self.articles_content_file = articles_content_file
        self.article_links = []

    def save_content(self, articles_content):
        """
        writing the articles to a file
        :param articles_content:

        """
        self.file_handler.write_news_files(self.article_links, articles_content, self.articles_list_file, self.articles_content_file)

    def get_relevant_content(self):
        """
        getting all the urls that we didn't already write to file

        """
        articles_list = set(self.file_handler.get_from_json(self.articles_list_file))
        return [url for url in self.article_links if url not in articles_list]
