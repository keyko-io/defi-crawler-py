from deficrawler.lending.querys import Querys
from deficrawler.lending.mappers.borrows import Mappers
from deficrawler.constants import Constants

import requests
import json


class Deposits:
    def __init__(self, protocol):
        self.protocol = protocol
        self.query_from_timestamp = Querys.DEPOSITS_FROM_TIMESTAMP[protocol]
        self.path = Constants.PATH_DEPOSITS[protocol]
        self.timestamp = Constants.TIMESTAMP[protocol]
        self.endpoint = Constants.ENDPOINT[protocol]

    def get_deposits_from(self, from_date, to_date):
        from_timestamp = timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y').strftime("%s"))

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y').strftime("%s"))

        deposits_json = get_data_from(query_input=self.query_from_timestamp,
                                      endpoint=self.endpoint,
                                      from_timestamp=from_timestamp,
                                      to_timestamp=to_timestamp,
                                      path=self.path,
                                      timestamp_name=self.timestamp)

        return Mappers.map_deposit(deposits_json, self.protocol)
