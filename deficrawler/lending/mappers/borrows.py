from deficrawler.lending.borrow import Borrow
import pkgutil

import json
import dict_digger


class Mappers:

    @staticmethod
    def map_borrow(json_data, protocol):
        list_borrows = []

        data = pkgutil.get_data(__name__, protocol.lower() + ".json")
        map_file = json.loads(data.decode())

        for ele in json_data:
            borrow = Borrow(
                dict_digger.dig(
                    ele,
                    *map_file['borrow']['attributes']['user']),
                dict_digger.dig(
                    ele,
                    *map_file['borrow']['attributes']['token']),
                dict_digger.dig(
                    ele,
                    *map_file['borrow']['attributes']['amount']),
                dict_digger.dig(
                    ele,
                    *map_file['borrow']['attributes']['timestamp']),
                protocol)

            list_borrows.append(borrow.to_dict())

        return list_borrows
