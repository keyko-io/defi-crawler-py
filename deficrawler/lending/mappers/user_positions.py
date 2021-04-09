from deficrawler.lending.user_position import UserPosition

import json


class Mappers:

    @staticmethod
    def map_user_positions(json_data, protocol):
        if(protocol == 'AAVE'):
            return Mappers.map_user_positions_aave(json_data, protocol)

    @staticmethod
    def map_user_positions_aave(json_data, protocol):
        list_user_positions = []
        for ele in json_data:
            user_positions = UserPosition(ele['user']['id'],
                                          ele['reserve']['symbol'],
                                          ele['currentTotalDebt'],
                                          ele['currentATokenBalance'],
                                          protocol)

            list_user_positions.append(user_positions.to_dict())

        return list_user_positions
