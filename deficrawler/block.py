from deficrawler.protocol_base import ProtocolBase


class Block(ProtocolBase):
    """
    Class to get data for the blockchain blocks
    """

    def __init__(self, protocol, chain, version):
        super().__init__(
            protocol=protocol,
            chain=chain,
            version=version
        )
        self.protocol_type = "blocks"

    def get_block_at_timestamp(self, timestamp):
        """
        Gets the block number for a specific timestamp
        """

        config = super().get_protocol_config('block')

        response_data = super().query_first_element(
            entity='block',
            timestamp=timestamp,
            aditional_filters=''
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
