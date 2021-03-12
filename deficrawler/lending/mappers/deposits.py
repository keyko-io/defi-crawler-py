from deficrawler.lending.deposit import Deposit

import json


class Mappers:

    @staticmethod
    def map_deposit(json_data, protocol):
        if(protocol == 'AAVE'):
            return Mappers.map_deposit_aave(json_data, protocol)
        if(protocol == 'COMPOUND'):
            return Mappers.map_deposit_compound(json_data, protocol)
        if(protocol == 'MAKER'):
            return Mappers.map_deposit_maker(json_data, protocol)
        if(protocol == 'CREAM'):
            return Mappers.map_deposit_cream(json_data, protocol)

    @staticmethod
    def map_deposit_aave(json_data, protocol):
        list_deposits = []
        for ele in json_data:
            deposit = Deposit(ele['user']['id'],
                              ele['reserve']['symbol'],
                              ele['amount'],
                              ele['timestamp'],
                              protocol)

            list_deposits.append(deposit.to_dict())

        return list_deposits

    @staticmethod
    def map_deposit_compound(json_data, protocol):
        list_deposits = []
        for ele in json_data:
            deposit = Deposit(ele['to'],
                              ele['cTokenSymbol'],
                              ele['underlyingAmount'],
                              ele['blockTime'],
                              protocol)

            list_deposits.append(deposit.to_dict())

        return list_deposits

    @staticmethod
    def map_deposit_maker(json_data, protocol):
        list_deposits = []
        for ele in json_data:
            deposit = Deposit(ele['owner']['address'],
                              'DAI',
                              ele['debt'],
                              ele['openedAt'],
                              protocol)

            list_deposits.append(deposit.to_dict())

        return list_deposits

    @staticmethod
    def map_deposit_cream(json_data, protocol):
        list_deposits = []
        for ele in json_data:
            deposit = Deposit(ele['to'],
                              ele['cTokenSymbol'],
                              ele['underlyingAmount'],
                              ele['blockTime'],
                              protocol)

            list_deposits.append(deposit.to_dict())

        return list_deposits
