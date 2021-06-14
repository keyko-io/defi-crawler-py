import dict_digger


class Transformer:
    """
    This class applies the transformations defined in the json config.
    Apply the specified function to transform the data from the subgraph to
    the common model format.
    """

    def __init__(self):
        """
        Constructor. Defines the dictionary that will be use to link the function name specified
        in the config file to the class function to apply.
        """
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
            "chainlink_prices": self.chainlink_prices,
            "concat_symbols": self.concat_symbols,
            "concat_list_symbols": self.concat_list_symbols,
            "rates_units_aave": self.rates_units_aave,
            "rates_units_comp": self.rates_units_comp,
            "rates_na": self.rates_na
        }

    def transform(self, element, common_field, protocol_field, transformations, query_elements):
        """
        Main function, is called from the mapper, if the field to map has a transformation function
        contained in the class dictionary, the specified function will be applied, in other case
        the value will be returned without modification.
        """
        if common_field in transformations:
            type_transformer = transformations[common_field]
            return self.transformers[type_transformer](common_field, element, protocol_field, query_elements)
        else:
            return dict_digger.dig(
                element,
                *protocol_field)

    def transform_decimals_field(self, common_field, element, protocol_field, query_elements, field):
        """
        Transform the decimals of the number, dividing the field for the decimals value in the subgraph response
        """
        decimals_field = query_elements[field]
        dec_value = dict_digger.dig(
            element,
            *decimals_field)

        protocol_amount = dict_digger.dig(
            element,
            *protocol_field)

        return float(protocol_amount) / 10 ** float(dec_value)

    def transform_decimals(self, common_field, element, protocol_field, query_elements):
        """
        Use the transform_decimals_field function to transform the decimals in the `decimals` field
        """
        return self.transform_decimals_field(common_field, element, protocol_field, query_elements, 'decimals')

    def transform_principal_decimals(self, common_field, element, protocol_field, query_elements):
        """
        Use the transform_decimals_field function to transform the decimals in the `principal_decimals` field
        """
        return self.transform_decimals_field(common_field, element, protocol_field, query_elements, 'principal_decimals')

    def transform_collateral_decimals(self, common_field, element, protocol_field, query_elements):
        """
        Use the transform_decimals_field function to transform the decimals in the `collateral_decimals` field
        """
        return self.transform_decimals_field(common_field, element, protocol_field, query_elements, 'collateral_decimals')

    def from_token_selection(self, common_field, element, protocol_field, query_elements):
        """
        Gets the from token in a swap, gets the field with amount != 0
        """
        amount_0_in = dict_digger.dig(
            element,
            *query_elements['from_token_amount'][0])

        index = 0 if float(amount_0_in) > 0 else 1

        return dict_digger.dig(
            element,
            *query_elements['from_token'][index])

    def to_token_selection(self, common_field, element, protocol_field, query_elements):
        """
        Gets the to token in a swap, gets the field with amount != 0
        """
        amount_0_out = dict_digger.dig(
            element,
            *query_elements['to_token_amount'][0])

        index = 0 if float(amount_0_out) > 0 else 1

        return dict_digger.dig(
            element,
            *query_elements['to_token'][index])

    def from_token_amount_selection(self, common_field, element, protocol_field, query_elements):
        """
        Gets the from token amount in a swap, gets the field with amount != 0
        """
        amount_0_in = dict_digger.dig(
            element,
            *query_elements['from_token_amount'][0])

        return amount_0_in if float(amount_0_in) > 0 else dict_digger.dig(
            element,
            *query_elements['from_token_amount'][1])

    def to_token_amount_selection(self, common_field, element, protocol_field, query_elements):
        """
        Gets the to token amount in a swap, gets the field with amount != 0
        """
        amount_0_out = dict_digger.dig(
            element,
            *query_elements['to_token_amount'][0])

        return amount_0_out if float(amount_0_out) > 0 else dict_digger.dig(
            element,
            *query_elements['to_token_amount'][1])

    def array_length(self, common_field, element, protocol_field, query_elements):
        """
        Returns the length of a field of array type
        """
        array_field = dict_digger.dig(
            element,
            query_elements[common_field][0])

        return len(array_field)

    def remove_token_prefix(self, common_field, element, protocol_field, query_elements):
        """
        Removes the token prefix of the token. Usefull to remove cTOkens or aTokens
        """
        field = dict_digger.dig(
            element,
            *query_elements[common_field])

        return field[1:]

    def tx_id_colon(self, common_field, element, protocol_field, query_elements):
        """
        Removes the trailing data afeter the : in the transaction id field
        """
        field = dict_digger.dig(
            element,
            *query_elements[common_field])

        return field.split(':')[0]

    def tx_id_hyphen(self, common_field, element, protocol_field, query_elements):
        """
        Removes the trailing data afeter the - in the transaction id field
        """
        field = dict_digger.dig(
            element,
            *query_elements[common_field])

        return field.split('-')[0]

    def chainlink_prices(self, common_field, element, protocol_field, query_elements):
        """
        Returns the chainlink prices in the correct format, if ETH pair are 18 decimals
        in other case 8 decimals
        """
        price = dict_digger.dig(
            element,
            *query_elements[common_field])

        pair = dict_digger.dig(
            element,
            *['assetPair', 'id'])

        pair_decimals = 8
        tokens = pair.split('/')
        if len(tokens) > 1:
            if(tokens[1] == 'ETH'):
                pair_decimals = 18

        return float(price) / 10 ** pair_decimals

    def concat_symbols(self, common_field, element, protocol_field, query_elements):
        """
        Return the list of symbols of the pool concatenated
        """
        tokens_concat = ''
        tokens_list = query_elements[common_field]

        for index, token_path in enumerate(tokens_list):
            token = dict_digger.dig(
                element,
                *token_path)
            tokens_concat += token
            if(index + 1) < len(tokens_list):
                tokens_concat += '/'

        return tokens_concat

    def concat_list_symbols(self, common_field, element, protocol_field, query_elements):
        """
        Return the list of symbols of the pool concatenated
        """
        tokens_concat = ''

        tokens_list = dict_digger.dig(
            element,
            query_elements[common_field][0])

        field_name = query_elements[common_field][1]

        for index, token in enumerate(tokens_list):
            tokens_concat += token[field_name]
            if(index + 1) < len(tokens_list):
                tokens_concat += '/'

        return tokens_concat

    def rates_units_aave(self, common_field, element, protocol_field, query_elements):
        """
        Return the aave rates units converted
        """

        rate = dict_digger.dig(
            element,
            *query_elements[common_field])

        return float(rate)/1e25

    def rates_units_comp(self, common_field, element, protocol_field, query_elements):
        """
        Return the comp rates units converted
        """

        rate = dict_digger.dig(
            element,
            *query_elements[common_field])

        return float(rate) * 1e2

    def rates_na(self, common_field, element, protocol_field, query_elements):
        """
        Return zero to not applicable rate value
        """

        return 0
