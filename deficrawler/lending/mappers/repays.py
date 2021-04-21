from deficrawler.lending.repay import Repay

import pkgutil
import json
import dict_digger


class Mappers:

    @staticmethod
    def map_repay(json_data, protocol):
        list_repays = []

        data = pkgutil.get_data('deficrawler.config', protocol.lower() + ".json")
        map_file = json.loads(data.decode())

        for ele in json_data:
            repay = Repay(
                dict_digger.dig(
                    ele,
                    *map_file['repay']['attributes']['user']),
                dict_digger.dig(
                    ele,
                    *map_file['repay']['attributes']['token']),
                dict_digger.dig(
                    ele,
                    *map_file['repay']['attributes']['amount']),
                dict_digger.dig(
                    ele,
                    *map_file['repay']['attributes']['timestamp']),
                protocol)

            list_repays.append(repay.to_dict())

        return list_repays
