from deficrawler.lending.querys import Querys
from deficrawler.constants import Constants
from deficrawler.lending.mappers.repays import Mappers
from deficrawler.api_calls import get_data_from


import requests
import json
from datetime import date, datetime


class Repays:
    def __init__(self, protocol):
        self.protocol = protocol
        self.query_from_timestamp = Querys.REPAYS_FROM_TIMESTAMP[protocol]
        self.path = Constants.PATH_REPAYS[protocol]
        self.timestamp = Constants.TIMESTAMP[protocol]
        self.endpoint = Constants.ENDPOINT[protocol]

    def get_repays_from(self, from_date, to_date):
        from_timestamp = timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y').strftime("%s"))

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y').strftime("%s"))

        repays_json = get_data_from(query_input=self.query_from_timestamp,
                                    endpoint=self.endpoint,
                                    from_timestamp=from_timestamp,
                                    to_timestamp=to_timestamp,
                                    path=self.path,
                                    timestamp_name=self.timestamp)

        return Mappers.map_repay(repays_json, self.protocol)
