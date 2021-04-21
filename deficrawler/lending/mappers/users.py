from deficrawler.lending.user import User

import json
import pkgutil
import dict_digger


class Mappers:

    @staticmethod
    def map_user(json_data, protocol):
        list_users = []

        data = pkgutil.get_data('deficrawler.config', protocol.lower() + ".json")
        map_file = json.loads(data.decode())

        for ele in json_data:
            user = User(
                dict_digger.dig(
                    ele,
                    *map_file['user']['attributes']['user_id']),
                dict_digger.dig(
                    ele,
                    *map_file['user']['attributes']['active_loans']),
                dict_digger.dig(
                    ele,
                    *map_file['user']['attributes']['liquidations_count']),
                protocol)

            list_users.append(user.to_dict())

        return list_users
