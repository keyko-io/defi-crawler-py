from deficrawler.lending.liquidation import Liquidation

import pkgutil
import json
import dict_digger


class Mappers:

    @staticmethod
    def map_liquidation(json_data, protocol):
        list_liquidations = []

        data = pkgutil.get_data('deficrawler.config',
                                protocol.lower() + ".json")
        map_file = json.loads(data.decode())

        for ele in json_data:
            liquidation = Liquidation(
                dict_digger.dig(
                    ele,
                    *map_file['liquidation']['attributes']['user']),
                dict_digger.dig(
                    ele,
                    *map_file['liquidation']['attributes']['token_principal']),
                dict_digger.dig(
                    ele,
                    *map_file['liquidation']['attributes']['token_collateral']),
                dict_digger.dig(
                    ele,
                    *map_file['liquidation']['attributes']['amount_principal']),
                dict_digger.dig(
                    ele,
                    *map_file['liquidation']['attributes']['amount_collateral']),
                dict_digger.dig(
                    ele,
                    *map_file['liquidation']['attributes']['liquidator']),
                dict_digger.dig(
                    ele,
                    *map_file['liquidation']['attributes']['timestamp']),
                protocol)

            list_liquidations.append(liquidation.to_dict())

        return list_liquidations
