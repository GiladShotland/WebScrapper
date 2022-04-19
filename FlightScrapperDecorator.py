from Scrappers.FlightScrapper import *

class FlightScrapperDecorator:
    def __init__(self):
        self.scrapper = FlightScrapper()

    def run(self):
        self.scrapper.land_first_page()
        while True:
            self.scrapper.update_flights()

