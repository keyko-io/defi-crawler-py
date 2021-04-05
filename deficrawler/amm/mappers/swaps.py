from deficrawler.amm.swap import Swap

import json


class Mappers:

    @staticmethod
    def map_swaps(json_data, protocol):
        if(protocol == 'UNISWAP'):
            return Mappers.map_swap_uniswap(json_data, protocol)

    @staticmethod
    def map_swap_uniswap(json_data, protocol):
        list_swaps = []
        for ele in json_data:
            swap = Swap(ele['sender'],
                        ele['transaction']['id'],
                        ele['pair']['token0']['symbol'] if float(
                            ele['amount0In']) > 0 else ele['pair']['token1']['symbol'],
                        ele['pair']['token1']['symbol'] if float(
                            ele['amount0Out']) > 0 else ele['pair']['token1']['symbol'],
                        ele['amount0In'] if float(
                            ele['amount0In']) > 0 else ele['amount1In'],
                        ele['amount0Out'] if float(
                            ele['amount0Out']) > 0 else ele['amount1Out'],
                        ele['timestamp'],
                        protocol)

            list_swaps.append(swap.to_dict())

        return list_swaps
