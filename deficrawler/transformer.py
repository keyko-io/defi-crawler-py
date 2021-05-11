import dict_digger


class Transformer:

    def __init__(self):
        self.transformers = {
            "decimals": self.transform_decimals,
            "principal_decimals": self.transform_principal_decimals,
            "collateral_decimals": self.transform_collateral_decimals,
            "from_token": self.from_token_selection,
            "to_token": self.to_token_selection,
            "from_token_amount": self.from_token_amount_selection,
            "to_token_amount": self.to_token_amount_selection,
            "array_length": self.array_length,
            "remove_token_prefix": self.remove_token_prefix,
            "tx_id_colon": self.tx_id_colon,
            "tx_id_hyphen": self.tx_id_hyphen,
            "chainlink_prices": self.chainlink_prices
        }

    def transform(self, element, common_field, protocol_field, transformations, query_elements):

        if common_field in transformations:
            type_transformer = transformations[common_field]
            return self.transformers[type_transformer](common_field, element, protocol_field, query_elements)
        else:
            return dict_digger.dig(
                element,
                *protocol_field)

    def transform_decimals_field(self, common_field, element, protocol_field, query_elements, field):
        decimals_field = query_elements[field]
        dec_value = dict_digger.dig(
            element,
            *decimals_field)

        protocol_amount = dict_digger.dig(
            element,
            *protocol_field)

        return float(protocol_amount) / 10 ** float(dec_value)

    def transform_decimals(self, common_field, element, protocol_field, query_elements):
        return self.transform_decimals_field(common_field, element, protocol_field, query_elements, 'decimals')

    def transform_principal_decimals(self, common_field, element, protocol_field, query_elements):
        return self.transform_decimals_field(common_field, element, protocol_field, query_elements, 'principal_decimals')

    def transform_collateral_decimals(self, common_field, element, protocol_field, query_elements):
        return self.transform_decimals_field(common_field, element, protocol_field, query_elements, 'collateral_decimals')

    def from_token_selection(self, common_field, element, protocol_field, query_elements):
        amount_0_in = dict_digger.dig(
            element,
            *query_elements['from_token_amount'][0])

        index = 0 if float(amount_0_in) > 0 else 1

        return dict_digger.dig(
            element,
            *query_elements['from_token'][index])

    def to_token_selection(self, common_field, element, protocol_field, query_elements):
        amount_0_out = dict_digger.dig(
            element,
            *query_elements['to_token_amount'][0])

        index = 0 if float(amount_0_out) > 0 else 1

        return dict_digger.dig(
            element,
            *query_elements['to_token'][index])

    def from_token_amount_selection(self, common_field, element, protocol_field, query_elements):
        amount_0_in = dict_digger.dig(
            element,
            *query_elements['from_token_amount'][0])

        return amount_0_in if float(amount_0_in) > 0 else dict_digger.dig(
            element,
            *query_elements['from_token_amount'][1])

    def to_token_amount_selection(self, common_field, element, protocol_field, query_elements):
        amount_0_out = dict_digger.dig(
            element,
            *query_elements['to_token_amount'][0])

        return amount_0_out if float(amount_0_out) > 0 else dict_digger.dig(
            element,
            *query_elements['to_token_amount'][1])

    def array_length(self, common_field, element, protocol_field, query_elements):
        array_field = dict_digger.dig(
            element,
            query_elements[common_field][0])

        return len(array_field)

    def remove_token_prefix(self, common_field, element, protocol_field, query_elements):
        field = dict_digger.dig(
            element,
            *query_elements[common_field])

        return field[1:]

    def tx_id_colon(self, common_field, element, protocol_field, query_elements):
        field = dict_digger.dig(
            element,
            *query_elements[common_field])

        return field.split(':')[0]

    def tx_id_hyphen(self, common_field, element, protocol_field, query_elements):
        field = dict_digger.dig(
            element,
            *query_elements[common_field])

        return field.split('-')[0]

    def chainlink_prices(self, common_field, element, protocol_field, query_elements):
        price = dict_digger.dig(
            element,
            *query_elements[common_field])

        pair = dict_digger.dig(
            element,
            *['assetPair', 'id'])

        pair_decimals = 8
        tokens = pair.split('/')
        if len(tokens)>1:
            if(tokens[1] == 'ETH'): pair_decimals = 18
        
        return float(price) / 10 ** pair_decimals