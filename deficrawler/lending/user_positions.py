from deficrawler.lending.querys import Querys
from deficrawler.lending.mappers.user_positions import Mappers
from deficrawler.constants import Constants
from deficrawler.api_calls import get_data_parameter


class UserPositions:
    def __init__(self, protocol):
        self.protocol = protocol
        self.query_positions = Querys.USERS_POSITIONS[protocol]
        self.path = Constants.PATH_POSITIONS[protocol]
        self.endpoint = Constants.ENDPOINT[protocol]

    def get_positions(self, user_id):
        user_position_json = get_data_parameter(query_input=self.query_positions,
                                                endpoint=self.endpoint,
                                                path=self.path,
                                                parameter=user_id)

        return Mappers.map_user_positions(user_position_json, self.protocol)
