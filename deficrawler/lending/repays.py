from deficrawler.lending.querys import Querys
from deficrawler.constants import Constants
import requests
import json
from deficrawler.lending.mappers import Mappers


class Repays:
    def __init__(self, protocol):
        self.protocol = protocol
        self.query_from_timestamp = Querys.REPAYS_FROM_TIMESTAMP[protocol]
        self.path = Constants.PATH_REPAYS[protocol]
        self.timestamp = Constants.TIMESTAMP[protocol]
        self.endpoint = Constants.ENDPOINT[protocol]

    def get_repays_from_timestamp(self, timestamp=0):
        repays_json = self.get_repays_from_api(timestamp)
        return Mappers.map_repay(repays_json, self.protocol)

    def get_repays_from_api(self, timestamp=0):
        are_reserve = True
        json_records = []
        from_timestamp = timestamp

        while are_reserve:
            query = self.query_from_timestamp.format(from_timestamp)
            response = requests.post(self.endpoint, json={'query': query})
            json_data = json.loads(response.text)
            response_lenght = len(json_data['data'][self.path])
            if (response_lenght > 0):
                json_data = json.loads(response.text)
                list_reserves = json_data['data'][self.path]
                from_timestamp = json_data['data'][self.path][response_lenght -
                                                              1][self.timestamp]
                json_records = [*json_records, *list_reserves]
            else:
                are_reserve = False
        return json_records
