from deficrawler.lending.querys import Querys
from deficrawler.constants import Constants
from deficrawler.lending.mappers.borrows import Mappers
from deficrawler.api_calls import get_data_from
from deficrawler.utils import format_attribute

from datetime import date, datetime
import pkgutil
import json


class Borrows:
    def __init__(self, protocol):
        self.protocol = protocol
        self.query_from_timestamp = Querys.BORROWS_FROM_TIMESTAMP
        self.path = Constants.PATH_BORROWS[protocol]
        self.timestamp = Constants.TIMESTAMP[protocol]
        self.endpoint = Constants.ENDPOINT[protocol]

    def get_borrows_from(self, from_date, to_date):
        from_timestamp = timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y').strftime("%s"))

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y').strftime("%s"))

        borrows_json = get_data_from(query_input=self.query_from_timestamp,
                                     from_timestamp=from_timestamp,
                                     to_timestamp=to_timestamp,
                                     event="borrow",
                                     protocol=self.protocol)

        return Mappers.map_borrow(borrows_json, self.protocol)
