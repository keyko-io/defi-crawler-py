from deficrawler.protocol_base import ProtocolBase

from datetime import datetime


class Dex(ProtocolBase):
    """
    Class to get data for Dexes protocols
    """

    def __init__(self, protocol, chain, version):
        super().__init__(
            protocol=protocol,
            chain=chain,
            version=version
        )
        self.protocol_type = "dex"

    def get_data_from_date_range(self, from_date, to_date, entity, pool=''):
        """
        Gets data for the specified entity in the from_data to to_date period.
        The entities are defined in the configuration of each protocol.
        """

        from_timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y %H:%M:%S').timestamp())

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y %H:%M:%S').timestamp())

        config = super().get_protocol_config(entity)

        pool_filter = ''
        if(pool != ''):
            pool_filter = {
                self.mappings_file['entities'][entity]['query']['params']['pool']: pool
            }

        response_data = super().query_data_from_date_range(
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            entity=entity,
            aditional_filters=pool_filter
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )

    def get_all_pools(self):
        """
        Returns all pools of the protocol
        """

        config = super().get_protocol_config('pool')

        response_data = super().query_data_parameter(
            entity='pool'
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
