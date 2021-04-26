from deficrawler.querys import Querys
from deficrawler.mappers import Mappers
from deficrawler.api_calls import get_data_from

from datetime import date, datetime
import pkgutil
import json


class Protocol:
    def __init__(self, protocol):
        self.protocol = protocol
        self.query_from_timestamp = Querys.QUERY_FROM_TIMESTAMP
        config_file = pkgutil.get_data(
            'deficrawler.config',
            protocol.lower() + ".json"
        )

        self.mappings_file = json.loads(config_file.decode())

    def get_data_from_date_range(self, from_date, to_date, entity):

        from_timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y %H:%M:%S').strftime("%s"))

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y %H:%M:%S').strftime("%s"))

        attributes = self.mappings_file['entities'][entity]['attributes']
        transformations = self.mappings_file['entities'][entity]['transformations']
        transformations = self.mappings_file['entities'][entity]['transformations']
        query_elements = self.mappings_file['entities'][entity]['query']['fields']

        json_data = get_data_from(query_input=self.query_from_timestamp,
                                  from_timestamp=from_timestamp,
                                  to_timestamp=to_timestamp,
                                  entity=entity,
                                  mappings_file=self.mappings_file,
                                  protocol=self.protocol)

        return Mappers.map_data(json_data=json_data,
                                protocol=self.protocol,
                                entity=entity,
                                attributes=attributes,
                                transformations=transformations,
                                query_elements=query_elements)
