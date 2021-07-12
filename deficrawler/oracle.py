from deficrawler.protocol_base import ProtocolBase

from datetime import datetime


class Oracle(ProtocolBase):
    """
    Oracle class to get prices
    """

    def __init__(self, protocol, chain, version):
        super().__init__(
            protocol=protocol,
            chain=chain,
            version=version
        )

    def get_all_pairs(self):
        """
        Returns all the existing prices for the oracle.
        """

        config = super().get_protocol_config('pair')

        response_data = super().query_data_filtered(
            entity='pair',
            filters=''
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )

    def get_price_from_date_range(self, from_date, to_date, pair):
        """
        Returns the prices series for the specified pair in the given period
        """

        from_timestamp = int(
            datetime.strptime(from_date, '%d/%m/%Y %H:%M:%S').timestamp())

        to_timestamp = int(datetime.strptime(
            to_date, '%d/%m/%Y %H:%M:%S').timestamp())

        config = super().get_protocol_config('price')

        pair_name = self.mappings_file['entities']['price']['query']['params']['pair']

        response_data = super().query_data_from_date_range(
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            entity='price',
            aditional_filters={pair_name: pair}
        )

        return super().map_data(
            response_data=response_data,
            config=config
        )

    def get_price_at_timestamp(self, timestamp, pair):
        """
        Returns the prices for the specified pair in the given timestamp
        """

        config = super().get_protocol_config('price')

        pair_name = self.mappings_file['entities']['price']['query']['params']['pair']

        response_data = super().query_first_element(
            aditional_filters={pair_name: pair},
            entity='price',
            timestamp=timestamp
        )

        prices = super().map_data(
            response_data=response_data,
            config=config
        )

        if len(prices) > 0:
            return prices[0]['price']
        else:
            raise Exception(
                "Price not found for the specified pair at the timestamp")
