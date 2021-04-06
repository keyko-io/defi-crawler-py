from deficrawler.amm.swap import Swap

import json


class Mappers:

    @staticmethod
    def map_swaps(json_data, protocol):
        if(protocol == 'UNISWAP'):
            return Mappers.map_swap_uniswap(json_data, protocol)
        if(protocol == 'BALANCER'):
            return Mappers.map_swap_balancer(json_data, protocol)
        if(protocol == 'BANCOR'):
            return Mappers.map_swap_bancor(json_data, protocol)
        if(protocol == 'SUSHISWAP'):
            return Mappers.map_swap_sushiswap(json_data, protocol)
        if(protocol == 'KYBER'):
            return Mappers.map_swap_kyber(json_data, protocol)

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

    @staticmethod
    def map_swap_sushiswap(json_data, protocol):
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

    @staticmethod
    def map_swap_balancer(json_data, protocol):
        list_swaps = []
        for ele in json_data:
            swap = Swap(ele['userAddress']['id'],
                        ele['id'],
                        ele['tokenInSym'],
                        ele['tokenOutSym'],
                        ele['tokenAmountIn'],
                        ele['tokenAmountOut'],
                        ele['timestamp'],
                        protocol)

            list_swaps.append(swap.to_dict())

        return list_swaps

    @staticmethod
    def map_swap_bancor(json_data, protocol):
        list_swaps = []
        for ele in json_data:
            swap = Swap(ele['trader']['id'],
                        ele['transaction']['id'],
                        ele['fromToken']['symbol'],
                        ele['toToken']['symbol'],
                        ele['amountPurchased'],
                        ele['amountReturned'],
                        ele['timestamp'],
                        protocol)

            list_swaps.append(swap.to_dict())

        return list_swaps

    @staticmethod
    def map_swap_kyber(json_data, protocol):
        list_swaps = []
        for ele in json_data:
            swap = Swap(ele['trader']['id'],
                        ele['id'],
                        ele['src']['symbol'],
                        ele['dest']['symbol'],
                        ele['rawSrcAmount'],
                        ele['rawDestAmount'],
                        ele['createdAtBlockTimestamp'],
                        protocol)

            list_swaps.append(swap.to_dict())

        return list_swaps
