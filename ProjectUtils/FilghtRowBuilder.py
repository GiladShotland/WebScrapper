from ProjectUtils.Consts import *
from selenium.webdriver.common.by import By


class FlightRowBuilder:
    """
    class for parsing each row in the flights table
    """
    def build(self,row, type):
        """
        building a flight from a row by pulling the elements
        :param row: elements of row in the table
        :param type: arrive or depart
        :return: dictionary with the flight details
        """
        detailes = {'Airline Compant': self.get_airline(row)}
        if type == "arrive":
            detailes['Coming From'] = self.get_land(row)
        if type == "depart":
            detailes['Going To'] = self.get_land(row)

        detailes['Terminal'] = self.get_terminal(row)
        detailes['Scheduled Time'] = self.get_schedule(row)
        detailes['Estimated Time'] = self.get_updated_time(row)
        if type == "depart":
            detailes['Count'] = self.get_counter(row)

        detailes['Status'] = self.get_status(row)
        ans = {self.get_flight_num(row): detailes}
        return ans


    """
    Methods for getting the details from the elements - 
    Counter,Airline,Flight Number,Status,Land,Terminal,Schedule,Updated Time
    """
    def get_counter(self, row):
        counter_element = row.find_element(By.CSS_SELECTOR,'div[class="td-airline"]')
        counter = counter_element.get_attribute("innerText")
        return counter

    def get_airline(self, row):
        airline_element = row.find_element(By.CSS_SELECTOR, 'div[class="td-airline"]')
        airline = airline_element.get_attribute("innerText")
        return airline

    def get_flight_num(self, row):
        flight_num = row.find_element(By.CSS_SELECTOR, 'div[class="td-flight"]').get_attribute("innerText")
        return flight_num

    def get_status(self, row):
        status = row.find_element(By.CSS_SELECTOR, 'div[class="td-status"]').get_attribute("innerText")
        return status

    def get_land(self, row):
        land = row.find_element(By.CSS_SELECTOR, 'div[class="td-city"]').get_attribute("innerText")
        return land

    def get_terminal(self, row):
        terminal = row.find_element(By.CSS_SELECTOR, 'div[class="td-terminal"]').get_attribute("innerText")
        return terminal

    def get_schedule(self, row):
        schedule_element = row.find_element(By.CSS_SELECTOR, 'div[class="td-scheduledTime"]')
        time_schedule = schedule_element.find_element(By.TAG_NAME, 'time')
        hour_schedule = time_schedule.find_element(By.TAG_NAME, 'strong').get_attribute("innerText")
        date_schedule = time_schedule.find_element(By.TAG_NAME, 'div').get_attribute("innerText")
        total_schedule = hour_schedule + " " + date_schedule
        return total_schedule

    def get_updated_time(self, row):
        updated_time = row.find_element(By.CSS_SELECTOR, 'div[class="td-updatedTime"]').get_attribute("innerText")
        return updated_time

