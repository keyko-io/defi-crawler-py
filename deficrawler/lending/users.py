from deficrawler.lending.querys import Querys
from deficrawler.lending.mappers.users import Mappers
from deficrawler.constants import Constants
from deficrawler.api_calls import get_all_data


class Users:
    def __init__(self, protocol):
        self.protocol = protocol
        self.query_users = Querys.USERS[protocol]
        self.path = Constants.PATH_USERS[protocol]
        self.endpoint = Constants.ENDPOINT[protocol]
        self.order_by_name = Constants.PATH_USERS_ORDER[protocol]

    def get_users(self):
        users_json = get_all_data(query_input=self.query_users,
                                  endpoint=self.endpoint,
                                  path=self.path,
                                  order_by=0,
                                  order_by_name=self.order_by_name)

        return Mappers.map_user(users_json, self.protocol)
