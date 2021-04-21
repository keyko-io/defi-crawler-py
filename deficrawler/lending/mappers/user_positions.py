from deficrawler.lending.user_position import UserPosition

import json
import pkgutil
import dict_digger

class Mappers:

    @staticmethod
    def map_user_positions(json_data, protocol):
        if(protocol == 'AAVE'):
            return Mappers.map_user_positions_aave(json_data, protocol)

    @staticmethod
    def map_user_positions_aave(json_data, protocol):
        list_user_positions = []

        data = pkgutil.get_data('deficrawler.config',
                                protocol.lower() + ".json")
        map_file = json.loads(data.decode())

        for ele in json_data:
            user_position = UserPosition(
                dict_digger.dig(
                    ele,
                    *map_file['user_position']['attributes']['user_id']),
                dict_digger.dig(
                    ele,
                    *map_file['user_position']['attributes']['symbol']),
                dict_digger.dig(
                    ele,
                    *map_file['user_position']['attributes']['debt_amount']),
                dict_digger.dig(
                    ele,
                    *map_file['user_position']['attributes']['collateral_amount']),
                protocol)

            list_user_positions.append(user_position.to_dict())
        return list_user_positions
