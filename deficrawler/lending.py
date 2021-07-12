from deficrawler.block import Block
from deficrawler.protocol_base import ProtocolBase

from datetime import datetime


class Lending(ProtocolBase):
    """
    Class to get data for Lending protocols
    """

    def __init__(self, protocol, chain, version):
        super().__init__(
            protocol=protocol,
            chain=chain,
            version=version
        )
        self.protocol_type = "lending"

    def get_data_from_date_range(self, from_date, to_date, entity):
        """
        Gets data for the specified entity in the from_data to to_date period.
        The entities are defined in the configuration of each protocol.
        """

        from_timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y %H:%M:%S').timestamp())

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y %H:%M:%S').timestamp())

        config = super().get_protocol_config(entity)

        response_data = super().query_data_from_date_range(
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            entity=entity
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )

    def get_rates_from_date_range(self, from_date, to_date, entity, asset):
        """
        Gets rates data for the specified entity in the from_data to to_date period.
        """

        from_timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y %H:%M:%S').timestamp())

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y %H:%M:%S').timestamp())

        config = super().get_protocol_config(entity)

        asset_filter = {
            self.mappings_file['entities'][entity]['query']['params']['asset']: asset
        }

        filter_by_block = 'block' in self.mappings_file['entities'][entity]['query']['params']

        response_data = self.__get_data_from_blocks__(
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            entity=entity,
            aditional_filters=asset_filter
        ) if filter_by_block else super().query_data_from_date_range(
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            entity=entity,
            aditional_filters=asset_filter
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )

    def get_all_users(self):
        """
        Returns all the users of the protocol
        """

        config = super().get_protocol_config('user')

        response_data = super().query_data_parameter(
            entity='user'
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )

    def get_all_tokens(self):
        """
        Returns all the tokens of the protocol
        """

        config = super().get_protocol_config('token')

        response_data = super().query_data_parameter(
            entity='token'
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )

    def get_user_positions(self, user):
        """
        Returns the user positions (portfolio) of the given user
        """

        config = super().get_protocol_config('user_position')
        user_name = self.mappings_file['entities']['user_position']['query']['params']['user']

        response_data = super().query_data_filtered(
            entity='user_position',
            filters={user_name: user}
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )

    def supported_entities(self):
        """
        Returns the supported entities for the protocol
        """
        return super().supported_entities(self.protocol_type)

    def __get_data_from_blocks__(self, from_timestamp, to_timestamp, entity, aditional_filters):
        """
        Returns the data in the specific range querying block by block
        """
        blocks = Block(protocol='block', chain=self.chain,
                       version=1)

        block_start = int(blocks.get_block_at_timestamp(from_timestamp)[
            0]['number'])
        block_end = int(blocks.get_block_at_timestamp(
            to_timestamp)[0]['number'])

        data = []
        while(block_start < block_end):
            respose = super().query_first_element(entity=entity,
                                                  timestamp=from_timestamp,
                                                  aditional_filters=aditional_filters,
                                                  block=block_end)

            data = [*data,  *respose]
            if(len(respose) == 0 or int(respose[0]['blockTimestamp']) == 0):
                block_end = block_start
            else:
                updated_timestamp = respose[0]['blockTimestamp']
                block_end = int(blocks.get_block_at_timestamp(updated_timestamp)[
                    0]['number']) - 1

        return data
