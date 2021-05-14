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

    def get_data_from_date_range(self, from_date, to_date, entity):
        """
        Gets data for the specified entity in the from_data to to_date period.
        The entities are defined in the configuration of each protocol.
        """

        from_timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y %H:%M:%S').strftime("%s"))

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y %H:%M:%S').strftime("%s"))

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
