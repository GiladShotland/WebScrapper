import json
import os.path


class FilesHandler:
    """
    Class for handling the opening and writing for JSON files
    """
    def get_from_json(self, file_name):
        with open(file_name) as fn:
            return json.load(fn)

        return none

    def initialize_news_files(self, articles_list, articles_content):
        """initializing files for news Scrapper if needed"""
        if os.path.isfile(articles_list):
            return

        self.write_news_files([],{},articles_list,articles_content)

    def write_news_files(self, articles_set, articles_dict, articles_list, articles_content):
        with open(articles_list, 'w') as fw:
            json.dump(articles_set, fw)

        with open(articles_content, 'w') as fw:
            json.dump(articles_dict, fw)

    def initialize_flight_file(self, flights_diary):
        if os.path.isfile(flights_diary):
            return

        with open(flights_diary, 'w') as fw:
            json.dump([], fw)

    def append_flights(self, flights_diary, latest_flights):
        """appending the flights to the diary"""
        diary = self.get_from_json(flights_diary)
        diary.append(latest_flights)
        with open(flights_diary, 'w') as fw:
            json.dump(diary, fw)
