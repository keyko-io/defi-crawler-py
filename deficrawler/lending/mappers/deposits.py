from deficrawler.lending.deposit import Deposit

import pkgutil
import json
import dict_digger


class Mappers:

    @staticmethod
    def map_deposit(json_data, protocol):
        list_deposits = []

        data = pkgutil.get_data('deficrawler.config', protocol.lower() + ".json")
        map_file = json.loads(data.decode())

        for ele in json_data:
            deposit = Deposit(
                dict_digger.dig(
                    ele,
                    *map_file['deposit']['attributes']['user']),
                dict_digger.dig(
                    ele,
                    *map_file['deposit']['attributes']['token']),
                dict_digger.dig(
                    ele,
                    *map_file['deposit']['attributes']['amount']),
                dict_digger.dig(
                    ele,
                    *map_file['deposit']['attributes']['timestamp']),
                protocol)

            list_deposits.append(deposit.to_dict())

        return list_deposits
