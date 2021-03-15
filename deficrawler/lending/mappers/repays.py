from deficrawler.lending.repay import Repay

import json


class Mappers:

    @staticmethod
    def map_repay(json_data, protocol):
        if(protocol == 'AAVE'):
            return Mappers.map_repay_aave(json_data, protocol)
        if(protocol == 'COMPOUND'):
            return Mappers.map_repay_compound(json_data, protocol)
        if(protocol == 'MAKER'):
            return Mappers.map_repay_maker(json_data, protocol)
        if(protocol == 'CREAM'):
            return Mappers.map_repay_cream(json_data, protocol)

    @staticmethod
    def map_repay_aave(json_data, protocol):
        list_repays = []
        for ele in json_data:
            repay = Repay(ele['user']['id'],
                          ele['reserve']['symbol'],
                          ele['amount'],
                          ele['timestamp'],
                          protocol)

            list_repays.append(repay.to_dict())

        return list_repays

    @staticmethod
    def map_repay_compound(json_data, protocol):
        list_repays = []
        for ele in json_data:
            repay = Repay(ele['payer'],
                          ele['underlyingSymbol'],
                          ele['amount'],
                          ele['blockTime'],
                          protocol)

            list_repays.append(repay.to_dict())

        return list_repays

    @staticmethod
    def map_repay_maker(json_data, protocol):
        list_repays = []
        for ele in json_data:
            repay = Repay(ele['owner']['address'],
                          'DAI',
                          ele['debt'],
                          ele['openedAt'],
                          protocol)

            list_repays.append(repay.to_dict())

        return list_repays

    @staticmethod
    def map_repay_cream(json_data, protocol):
        list_repays = []
        for ele in json_data:
            repay = Repay(ele['payer'],
                          ele['underlyingSymbol'],
                          ele['amount'],
                          ele['blockTime'],
                          protocol)

            list_repays.append(repay.to_dict())

        return list_repays
