from deficrawler.amm.swap import Swap
from deficrawler.utils import get_token_symbol, get_token_amount

import pkgutil
import json
import dict_digger


class Mappers:

    @staticmethod
    def map_swaps(json_data, protocol):
        list_swaps = []

        data = pkgutil.get_data(
            'deficrawler.config',
            protocol.lower() + ".json")
            
        map_file = json.loads(data.decode())

        for ele in json_data:
            swap = Swap(
                dict_digger.dig(
                    ele,
                    *map_file['swap']['attributes']['user']),
                dict_digger.dig(
                    ele,
                    *map_file['swap']['attributes']['tx_id']),
                get_token_symbol(
                    ele,
                    map_file,
                    'from_token',
                    'from_token_amount'),
                get_token_symbol(ele, map_file, 'to_token', 'to_token_amount'),
                get_token_amount(ele, map_file, 'from_token_amount'),
                get_token_amount(ele, map_file, 'to_token_amount'),
                dict_digger.dig(
                    ele,
                    *map_file['swap']['attributes']['timestamp']),
                protocol)

            list_swaps.append(swap.to_dict())

        return list_swaps

   