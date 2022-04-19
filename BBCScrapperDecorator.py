from Scrappers.BBCScrapper import *
from Models.EmotionIdentifier import *
from Models.Summarizer import *
from ProjectUtils.Consts import *


class BBCScrapperDecorator:
    """
    decorator for applying Machine Learning models - they are pretty heavy for applying together with the scrapper
    """
    def __init__(self):
        self.articles_content = None
        self.articles = None

    def download_articles(self):
        """
        applying the scrapper
        """
        scrapper = BBCScrapper(teardown=True)
        scrapper.land_first_page()
        self.articles_content, self.articles = scrapper.download_articles()
        scrapper.save_content(articles_content=self.articles_content)

    def get_summary(self, url):
        """
        getting summary
        :param url: url of article
        :return: summary of the article, if exists
        """
        article = self.get_article_safe(url)
        if article is None:
            return None

        summarizer = Summarizer()
        return summarizer.get_summary(article)

    def get_emotion(self,url):
        """
        getting emotion from the model
        :param url: url of article
        :return: emotion of article
        """
        article = self.get_article_safe(url)
        if article is None:
            return None

        emotion_identifier = EmotionIdentifier()
        return emotion_identifier.identify_emotion(article)

    def get_article_safe(self,url):
        """
        validating if article exists
        :param url: url of article
        :return: article if exists, none otherwise
        """
        if url not in self.articles_content.keys():
            return None

        return self.articles_content[url]

    def search(self, query):
        """
        searching in whole articles
        :param query:
        :return:
        """

        for url in self.articles_content.keys():
            article = self.articles_content[url]
            if query in article:
                return url

        return "no article found"


