from deficrawler.api_calls import get_first_element
from deficrawler.querys import Querys
import pkgutil
import json


class Block():
    """
    Class to get data info for blocks
    """

    def __init__(self, protocol, chain):
        self.protocol = protocol
        self.query_first = Querys.QUERY_FIRST_ELEMENT
        self.blocks_file = self.__get_blocks_file()
        self.chain = chain
        self.endpoint = self.__get_blocks_endpoint(chain)

    def get_block_at_timestamp(self, timestamp):
        block_response = get_first_element(query_input=self.query_first,
                                           entity='block',
                                           mappings_file=self.blocks_file,
                                           endpoint=self.endpoint,
                                           timestamp=timestamp,
                                           aditional_filters='')

        if(len(block_response) > 0):
            return block_response[0]['number']
        else:
            raise Exception('Error getting the block number for the timestamp')

    def __get_blocks_file(self):
        """
        Gets the json file for blocks endpoints
        """
        try:
            config_file = pkgutil.get_data(
                'deficrawler.config',
                "blocks.json"
            )

        except FileNotFoundError:
            raise Exception('Blocks file not found')
        except:
            raise

        return json.loads(config_file.decode())

    def __get_blocks_endpoint(self, chain):
        """
        Gets the endpoint for the chain endpoint
        """
        try:
            return self.blocks_file['protocol']['endpoint'][chain.lower()]
        except KeyError:
            raise Exception('Protocol block file not supported')
        except:
            raise
