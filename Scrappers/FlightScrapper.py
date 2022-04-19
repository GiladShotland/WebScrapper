from Scrappers.Scrapper import *
from selenium.webdriver.common.by import By
from ProjectUtils.Consts import *
from ProjectUtils.FilghtRowBuilder import *
from ProjectUtils.FilesHandler import *


class FlightScrapper(Scrapper):
    def __init__(self, url=NATBAG_PATH, driver_path=CHROME_DRIVER_PATH, teardown=False):
        """initialize the scrapper and opening a diary"""
        super(FlightScrapper, self).__init__(url, driver_path, teardown)
        self.file_handler = FilesHandler()
        self.file_handler.initialize_flight_file(FLIGHTS_DIARY)
        self.last_time_updated = ""

    def update_flights(self):
        """getting flights if updated on the website, than updating the diary"""
        flights = self.get_flights()
        if flights is None:
            return

        self.file_handler.append_flights(FLIGHTS_DIARY, flights)

    def get_flights(self):
        """
        getting flights:
        if the time was updated, disable the updating on
        website and get the arrive and depart flights
        """
        curr_time = self.get_update_time()
        if curr_time != self.last_time_updated:
            self.last_time_updated = curr_time
            self.disable_enable_update()
            self.turn_arrival_mode()
            arrived_flights = self.get_flights_formatted("arrive")
            self.turn_depart_mode()
            depart_flights = self.get_flights_formatted("depart")
            ans_dict = {"time": curr_time, "arrivals:": arrived_flights, "departs:": depart_flights}
            self.disable_enable_update()
            return ans_dict

        return None

    def get_flights_formatted(self, type):
        """
        open the whole page, get the elements for each row and build a row from it
        :param type: arrive/depart
        :return: all the flights formatted {"flight number" : ...detials...}
        """
        self.scroll_whole_page()
        row_elements = self.get_row_elements()
        flights = []
        row_builder = FlightRowBuilder()
        cnt = 0
        for row in row_elements:
            flights.append(row_builder.build(row, type))
            cnt += 1




        return flights

    def turn_arrival_mode(self):
        """
        click on the arrival mode in the website

        """
        arrival_button = self.find_element(By.CSS_SELECTOR, 'a[id="tab--departures_flights-label"]')
        arrival_button.click()

    def turn_depart_mode(self):
        """
        click on depart mode on the website

        """
        depart_button = self.find_element(By.CSS_SELECTOR, 'a[id="tab--departures_flights-label"]')
        depart_button.click()

    def get_update_time(self):
        """
        getting last time the page was updated

        """
        time_element = self.find_element(By.ID, "lastUpdateTime")
        return time_element.get_attribute('innerText').split()[0]

    def scroll_whole_page(self):
        """
        open the whole flights table

        """
        next_button = self.find_element(By.CSS_SELECTOR, 'button[id="next"]')
        style_state = next_button.get_attribute("style")
        while style_state == "":
            next_button.click()
            button_next = self.find_element(By.CSS_SELECTOR, 'button[id="next"]')
            style_state = button_next.get_attribute("style")

    def disable_enable_update(self):
        """
        disable or enable the automatic update by clicking the button

        """
        button_update = self.find_element(By.CSS_SELECTOR, 'a[id="toggleAutoUpdate"][role="button"]')
        button_update.click()

    def get_row_elements(self):
        """
        getting the row elements

        """
        row_elements = self.find_elements(By.CSS_SELECTOR, 'tr[class^="flight_row"]')
        return row_elements

    def search(self,query):
        """
        search for query in the flights diary
        :param query: string
        :return: all the flights with this string
        """
        flights_array = self.file_handler.get_from_json(FLIGHTS_DIARY)
        ans = []
        for diary in flights_array:
            arrivals = diary['arrivals:']
            self.search_query_in_flights(query,arrivals,ans)
            departs = diary['departs:']
            self.search_query_in_flights(query,departs,ans)
        return ans


    def search_query_in_flights(self,query,diary,ans):
        """
        help method for searching
        """
        for flight in diary:
            for key in flight.keys():
                if key == query or query in flight[key].values():
                    ans.append((key, flight[key]))


if __name__ == '__main__':
    fs = FlightScrapper()
    print(fs.search("DL 9559"))


