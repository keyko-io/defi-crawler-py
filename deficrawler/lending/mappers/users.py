from deficrawler.lending.user import User

import json


class Mappers:

    @staticmethod
    def map_user(json_data, protocol):
        if(protocol == 'AAVE'):
            return Mappers.map_user_aave(json_data, protocol)

    @staticmethod
    def map_user_aave(json_data, protocol):
        list_users = []
        for ele in json_data:
            user = User(ele['id'],
                        ele['borrowedReservesCount'],
                        len(ele['liquidationCallHistory']),
                        protocol)

            list_users.append(user.to_dict())

        return list_users
