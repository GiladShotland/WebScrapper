from Bot import *
from Scrappers.consts import *
import json
from json_utils import *
from utils import *
from Models.Summarizer import Summarizer
from Models.EmotionIdentifier import EmotionIdentifier


class NewsScrapper(Scrapper):

    def __init__(self, url,articles_list_file,articles_content_file, driver_path=CHROME_DRIVER_PATH, teardown=False):
        initialize_files(articles_list_file, articles_content_file)
        super(NewsScrapper,self).__init__(url,driver_path,teardown)
        self.articles_list_file = articles_list_file
        self.articles_content_file = articles_content_file
        self.article_links = []
        self.summarizer = Summarizer()
        self.emotion_identifier = EmotionIdentifier()



    def download_articles(self):
        pass

    def extract_content(self):
        pass

    def save_content(self,articles_content):
        write_files(self.article_links, articles_content, self.articles_list_file, self.articles_content_file)

    def search(self, query) -> str:
        articles = get_from_json(self.articles_content_file)
        for url in articles.keys():
            article = articles[url]
            if query in article:
                return url

        return "no article found"

    def articles_summary(self) -> list[str]:
        articles = get_from_json(self.articles_content_file)
        summaries = []
        for url in articles.keys():
            summaries.append(self.summarizer.get_summay(articles[url]))
        return summaries

    def sentiment_analysis(self) -> list[str]:
        emotions = []
        articles = get_from_json(self.articles_content_file)
        for url in articles.keys():
            emotions.append(self.emotion_identifier.identify_emotion(articles[url]))

        return emotions


    def get_relevant_content(self):
        articles_list = set(get_from_json(self.articles_list_file))
        return get_distinct_elements(self.article_links,articles_list)

