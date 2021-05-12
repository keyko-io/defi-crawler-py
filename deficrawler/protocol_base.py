from deficrawler import protocol
from deficrawler.querys import Querys
from deficrawler.mappers import Mappers
from deficrawler.api_calls import get_data_from, get_data_parameter, get_data_filtered

import pkgutil
import json


class ProtocolBase:
    def __init__(self, protocol, chain, version):
        self.protocol = protocol
        self.query_from_timestamp = Querys.QUERY_FROM_TIMESTAMP
        self.query_all_elements = Querys.QUERY_ALL_ELEMENTS
        self.query_filter = Querys.QUERY_ELEMENT_FILTER
        self.mappings_file = self.__get_protocol_file(protocol, version)
        self.chain = chain
        self.version = version
        self.endpoint = self.__get_protocol_endpoint(chain)

    def query_data_from_date_range(self, from_timestamp, to_timestamp, entity, aditional_filters=''):

        return get_data_from(query_input=self.query_from_timestamp,
                             from_timestamp=from_timestamp,
                             to_timestamp=to_timestamp,
                             entity=entity,
                             mappings_file=self.mappings_file,
                             protocol=self.protocol,
                             endpoint=self.endpoint,
                             aditional_filters=aditional_filters)

    def query_data_parameter(self, entity):

        return get_data_parameter(query_input=self.query_all_elements,
                                  entity=entity,
                                  mappings_file=self.mappings_file,
                                  protocol=self.protocol,
                                  endpoint=self.endpoint)

    def query_data_filtered(self, entity, filters):

        return get_data_filtered(query_input=self.query_filter,
                                 entity=entity,
                                 mappings_file=self.mappings_file,
                                 protocol=self.protocol,
                                 endpoint=self.endpoint,
                                 filters=filters)

    def map_data(self, response_data, config):
        return Mappers.map_data(response_data=response_data,
                                protocol=self.protocol,
                                chain=self.chain,
                                version=self.version,
                                attributes=config['attributes'],
                                transformations=config['transformations'],
                                query_elements=config['query_elements'])

    def get_protocol_config(self, entity):

        self.__exists_entity(entity)

        query_elements = self.mappings_file['entities'][entity]['query']['extra_fields']
        query_elements.update(
            self.mappings_file['entities'][entity]['attributes'])

        return {
            'attributes': self.mappings_file['entities'][entity]['attributes'],
            'transformations': self.mappings_file['entities'][entity]['transformations'],
            'query_elements': query_elements,
        }

    def __get_protocol_file(self, protocol, version):
        try:
            config_file = pkgutil.get_data(
                'deficrawler.config',
                protocol.lower() + "-" + str(version) + ".json"
            )

        except FileNotFoundError:
            raise Exception('Protocol ' + protocol +
                            ' version ' + str(version) + ' not supported')
        except:
            raise

        return json.loads(config_file.decode())

    def __get_protocol_endpoint(self, chain):
        try:
            return self.mappings_file['protocol']['endpoint'][chain.lower()]
        except KeyError:
            raise Exception('Protocol ' + self.protocol +
                            ' chain ' + chain + ' not supported')
        except:
            raise

    def __exists_entity(self, entity):
        if entity in self.mappings_file['entities']:
            return True
        else:
            raise Exception('Entity ' + entity +
                            ' not supported for protocol ' + self.protocol)
