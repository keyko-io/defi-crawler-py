from deficrawler.querys import Querys
from deficrawler.mappers import Mappers
from deficrawler.api_calls import get_data_from, get_data_parameter, get_data_filtered, get_first_element

import pkgutil
import json


class ProtocolBase:
    """
    Parent class to be inherit from Protocol and oracle
    """

    def __init__(self, protocol, chain, version):
        self.protocol = protocol
        self.query_from_timestamp = Querys.QUERY_FROM_TIMESTAMP
        self.query_all_elements = Querys.QUERY_ALL_ELEMENTS
        self.query_filter = Querys.QUERY_ELEMENT_FILTER
        self.query_first = Querys.QUERY_FIRST_ELEMENT
        self.mappings_file = self.__get_protocol_file(protocol, version)
        self.chain = chain
        self.version = version
        self.endpoint = self.__get_protocol_endpoint(chain)
        self.global_config = self.__load_global_config()

    def query_data_from_date_range(self, from_timestamp, to_timestamp, entity, aditional_filters=''):
        """
        Gets all the data from the given entity and the specified period. One or more filters can be applied
        """

        return get_data_from(query_input=self.query_from_timestamp,
                             from_timestamp=from_timestamp,
                             to_timestamp=to_timestamp,
                             entity=entity,
                             mappings_file=self.mappings_file,
                             endpoint=self.endpoint,
                             aditional_filters=aditional_filters)

    def query_data_parameter(self, entity):
        """
        Gets all the existing data for the given entity
        """

        return get_data_parameter(query_input=self.query_all_elements,
                                  entity=entity,
                                  mappings_file=self.mappings_file,
                                  endpoint=self.endpoint)

    def query_data_filtered(self, entity, filters):
        """
        Gets all the existing data for the given entity with the specified filters
        """

        return get_data_filtered(query_input=self.query_filter,
                                 entity=entity,
                                 mappings_file=self.mappings_file,
                                 endpoint=self.endpoint,
                                 filters=filters)

    def query_first_element(self, entity, timestamp, aditional_filters, block=None):
        """
        Gets the first existing element for the given entity with the specified filters
        """
        return get_first_element(query_input=self.query_first,
                                 entity=entity,
                                 mappings_file=self.mappings_file,
                                 endpoint=self.endpoint,
                                 timestamp=timestamp,
                                 aditional_filters=aditional_filters,
                                 block=block)

    def map_data(self, response_data, config):
        """
        Maps the data from the subgraph data to the defined commom model in
        the json file
        """
        return Mappers.map_data(response_data=response_data,
                                protocol=self.protocol,
                                chain=self.chain,
                                version=self.version,
                                attributes=config['attributes'],
                                transformations=config['transformations'],
                                query_elements=config['query_elements'])

    def get_protocol_config(self, entity):
        """
        Gets the protocol config in the json file for the specified entity.
        If the entity not exists will raise an error.
        """

        self.__exists_entity(entity)

        query_elements = self.mappings_file['entities'][entity]['query']['extra_fields']
        query_elements.update(
            self.mappings_file['entities'][entity]['attributes'])

        return {
            'attributes': self.mappings_file['entities'][entity]['attributes'],
            'transformations': self.mappings_file['entities'][entity]['transformations'],
            'query_elements': query_elements,
        }

    def supported_entities(self, protocol_type):
        """
        Returns an array with the supported entities for each type of protocol
        """
        supported = []
        protocol_type_entities = self.global_config['supported_entities'][protocol_type]
        for attr, _ in self.mappings_file['entities'].items():
            if attr in protocol_type_entities:
                supported.append(attr)

        return supported

    def __get_protocol_file(self, protocol, version):
        """
        Gets the json file for the specified protocol and the specified version.
        If the protocol does not exits at this version will raise an error.
        """
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
        """
        Gets the endpoint for the specified chain.
        If the chain does not exits in the config file will raise an error.
        """
        try:
            return self.mappings_file['protocol']['endpoint'][chain.lower()]
        except KeyError:
            raise Exception('Protocol ' + self.protocol +
                            ' chain ' + chain + ' not supported')
        except:
            raise

    def __exists_entity(self, entity):
        """
        Checks if the given entity exists in the entities config.
        In not exists will raise an error.
        """
        if entity in self.mappings_file['entities']:
            return True
        else:
            raise Exception('Entity ' + entity +
                            ' not supported for protocol ' + self.protocol)

    def __load_global_config(self):
        """
        Loads the global config file
        """
        try:
            global_config_file = pkgutil.get_data(
                "deficrawler.config",
                "global.json"
            )

        except FileNotFoundError:
            raise Exception('Error loading global config')
        except:
            raise

        return json.loads(global_config_file.decode())
