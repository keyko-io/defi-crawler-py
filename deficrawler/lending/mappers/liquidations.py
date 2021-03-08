from deficrawler.lending.liquidation import Liquidation

import json


class Mappers:

    @staticmethod
    def map_liquidation(json_data, protocol):
        if(protocol == 'AAVE'):
            return Mappers.map_liquidation_aave(json_data, protocol)
        if(protocol == 'COMPOUND'):
            return Mappers.map_liquidation_compound(json_data, protocol)
        if(protocol == 'MAKER'):
            return Mappers.map_liquidation_maker(json_data, protocol)
        if(protocol == 'CREAM'):
            return Mappers.map_liquidation_cream(json_data, protocol)

    @staticmethod
    def map_liquidation_aave(json_data, protocol):
        list_liquidations = []
        for ele in json_data:
            liquidation = Liquidation(ele['user']['id'],
                                      ele['principalReserve']['symbol'],
                                      ele['collateralReserve']['symbol'],
                                      ele['principalAmount'],
                                      ele['collateralAmount'],
                                      ele['liquidator'],
                                      ele['timestamp'],
                                      protocol)

            list_liquidations.append(liquidation.to_dict())

        return list_liquidations

    @staticmethod
    def map_liquidation_compound(json_data, protocol):
        list_liquidations = []
        for ele in json_data:
            liquidation = Liquidation(ele['from'],
                                      ele['underlyingSymbol'],
                                      ele['cTokenSymbol'],
                                      ele['underlyingRepayAmount'],
                                      ele['amount'],
                                      ele['to'],
                                      ele['blockTime'],
                                      protocol)

            list_liquidations.append(liquidation.to_dict())

        return list_liquidations

    @staticmethod
    def map_liquidation_cream(json_data, protocol):
        list_liquidations = []
        for ele in json_data:
            liquidation = Liquidation(ele['from'],
                                      ele['underlyingSymbol'],
                                      ele['cTokenSymbol'],
                                      ele['underlyingRepayAmount'],
                                      ele['amount'],
                                      ele['to'],
                                      ele['blockTime'],
                                      protocol)

            list_liquidations.append(liquidation.to_dict())

        return list_liquidations
