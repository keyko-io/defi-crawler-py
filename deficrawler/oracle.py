from deficrawler.querys import Querys
from deficrawler.mappers import Mappers
from deficrawler.api_calls import get_data_from, get_data_parameter, get_data_filtered

from datetime import date, datetime
import pkgutil
import json


class Oracle:
    def __init__(self, protocol, chain, version):
        self.protocol = protocol
        self.query_from_timestamp = Querys.QUERY_FROM_TIMESTAMP
        self.query_all_elements = Querys.QUERY_ALL_ELEMENTS
        self.query_filter = Querys.QUERY_ELEMENT_FILTER
        config_file = pkgutil.get_data(
            'deficrawler.config',
            protocol.lower() + "-" + str(version) + ".json"
        )

        self.mappings_file = json.loads(config_file.decode())
        self.chain = chain
        self.version = version
        self.endpoint = self.mappings_file['protocol']['endpoint'][chain.lower(
        )]

    def get_all_pairs(self):

        config = self.__get_protocol_config('pair')

        json_data = get_data_filtered(query_input=self.query_filter,
                                      entity='pair',
                                      mappings_file=self.mappings_file,
                                      protocol=self.protocol,
                                      endpoint=self.endpoint,
                                      filters='')

        return Mappers.map_data(json_data=json_data,
                                protocol=self.protocol,
                                chain=self.chain,
                                version=self.version,
                                entity='pair',
                                attributes=config['attributes'],
                                transformations=config['transformations'],
                                query_elements=config['query_elements'])

    def get_price_from_date_range(self, from_date, to_date, pair):

        from_timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y %H:%M:%S').strftime("%s"))

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y %H:%M:%S').strftime("%s"))

        config = self.__get_protocol_config('price')

        pair_name = self.mappings_file['entities']['price']['query']['params']['pair']

        json_data = get_data_from(query_input=self.query_from_timestamp,
                                  from_timestamp=from_timestamp,
                                  to_timestamp=to_timestamp,
                                  entity='price',
                                  mappings_file=self.mappings_file,
                                  protocol=self.protocol,
                                  endpoint=self.endpoint,
                                  aditional_filters={pair_name: pair})

        return Mappers.map_data(json_data=json_data,
                                protocol=self.protocol,
                                chain=self.chain,
                                version=self.version,
                                entity='price',
                                attributes=config['attributes'],
                                transformations=config['transformations'],
                                query_elements=config['query_elements'])

    def get_price_at_timestamp(self, timestamp, pair):

        config = self.__get_protocol_config('price')

        json_data = get_data_from(query_input=self.query_from_timestamp,
                                  from_timestamp=from_timestamp,
                                  to_timestamp=to_timestamp,
                                  entity='price',
                                  mappings_file=self.mappings_file,
                                  protocol=self.protocol,
                                  endpoint=self.endpoint)

        return Mappers.map_data(json_data=json_data,
                                protocol=self.protocol,
                                chain=self.chain,
                                version=self.version,
                                entity='price',
                                attributes=config['attributes'],
                                transformations=config['transformations'],
                                query_elements=config['query_elements'])

    def __get_protocol_config(self, entity):

        query_elements = self.mappings_file['entities'][entity]['query']['extra_fields']
        query_elements.update(
            self.mappings_file['entities'][entity]['attributes'])

        return {
            'attributes': self.mappings_file['entities'][entity]['attributes'],
            'transformations': self.mappings_file['entities'][entity]['transformations'],
            'query_elements': query_elements,
        }
