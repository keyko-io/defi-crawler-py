from deficrawler.lending.querys import Querys
from deficrawler.constants import Constants
import requests
import json
from datetime import date, datetime
from deficrawler.lending.mappers import Mappers


class Borrows:
    def __init__(self, protocol):
        self.protocol = protocol
        self.query_from_timestamp = Querys.BORROWS_FROM_TIMESTAMP[protocol]
        self.path = Constants.PATH_BORROWS[protocol]
        self.timestamp = Constants.TIMESTAMP[protocol]
        self.endpoint = Constants.ENDPOINT[protocol]

    def get_borrows_from(self, from_date, to_date):
        from_timestamp = timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y').strftime("%s"))
        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y').strftime("%s"))
        borrows_json = self.get_borrows_from_api(from_timestamp, to_timestamp)
        return Mappers.map_borrow(borrows_json, self.protocol)

    def get_borrows_from_api(self, from_timestamp, to_timestamp):
        are_reserve = True
        json_records = []
        iteration_timestamp = from_timestamp

        while are_reserve:
            query = self.query_from_timestamp.format(
                iteration_timestamp, to_timestamp)
            response = requests.post(self.endpoint, json={'query': query})
            json_data = json.loads(response.text)
            response_lenght = len(json_data['data'][self.path])
            if (response_lenght > 0):
                json_data = json.loads(response.text)
                list_reserves = json_data['data'][self.path]
                iteration_timestamp = json_data['data'][self.path][response_lenght -
                                                                   1][self.timestamp]

                json_records = [*json_records, *list_reserves]
            else:
                are_reserve = False
        return json_records
