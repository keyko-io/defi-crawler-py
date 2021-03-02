import json
from deficrawler.borrow import Borrow


class Mappers:

    @staticmethod
    def map_borrow(json_data, protocol):
        if(protocol == 'AAVE'):
            return Mappers.map_borrow_aave(json_data, protocol)
        if(protocol == 'COMPOUND'):
            return Mappers.map_borrow_compound(json_data, protocol)
        if(protocol == 'MAKER'):
            return Mappers.map_borrow_maker(json_data, protocol)
        if(protocol == 'CREAM'):
            return Mappers.map_borrow_cream(json_data, protocol)

    @staticmethod
    def map_borrow_aave(json_data, protocol):
        list_borrows = []
        for ele in json_data:
            borrow = Borrow(ele['user']['id'],
                            ele['reserve']['symbol'],
                            ele['amount'],
                            ele['timestamp'],
                            protocol)

            list_borrows.append(borrow.to_dict())

        return list_borrows

    @staticmethod
    def map_borrow_compound(json_data, protocol):
        list_borrows = []
        for ele in json_data:
            borrow = Borrow(ele['borrower'],
                            ele['underlyingSymbol'],
                            ele['amount'],
                            ele['blockTime'],
                            protocol)

            list_borrows.append(borrow.to_dict())

        return list_borrows

    @staticmethod
    def map_borrow_maker(json_data, protocol):
        list_borrows = []
        for ele in json_data:
            borrow = Borrow(ele['owner']['address'],
                            'DAI',
                            ele['debt'],
                            ele['openedAt'],
                            protocol)

            list_borrows.append(borrow.to_dict())

        return list_borrows

    @staticmethod
    def map_borrow_cream(json_data, protocol):
        list_borrows = []
        for ele in json_data:
            borrow = Borrow(ele['borrower'],
                            ele['underlyingSymbol'],
                            ele['amount'],
                            ele['blockTime'],
                            protocol)

            list_borrows.append(borrow.to_dict())

        return list_borrows
