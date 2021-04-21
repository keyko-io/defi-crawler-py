import dict_digger


def get_attributes(event, map_file):
    list_attr = ''
    attributes = map_file[event]['attributes']
    for attribute, value in attributes.items():
        list_attr += format_attribute(value) + " "
    return list_attr


def format_element(list_elements):
    if(len(list_elements) == 1):
        return list_elements[0]

    path = list_elements[0] + '{'
    for index, field in enumerate(list_elements):
        if index > 0 and index % 2 != 0:
            path += field
        if index > 0 and index % 2 == 0:
            path += '{'+field+'}'

    path += '}'
    return path


def format_attribute(list_fields):
    str_list_attr = ""

    if(isinstance(list_fields[0], list)):
        for list_elements in list_fields:
            str_list_attr += format_element(list_elements) + " "
    else:
        str_list_attr += format_element(list_fields)
    return str_list_attr


def get_token_symbol(ele, map_file, path_symbol, path_amount):

    tokens_symbols = map_file['swap']['attributes'][path_symbol]

    if not(isinstance(tokens_symbols[0], list)):
        return tokens_symbols[0]

    tokens_amounts = [
        dict_digger.dig(
            ele,
            *map_file['swap']['attributes'][path_amount][0]),
        dict_digger.dig(
            ele,
            *map_file['swap']['attributes'][path_amount][1])
    ]

    index = 0
    if(float(tokens_amounts[1]) > 0):
        index = 1

    return dict_digger.dig(
        ele,
        *map_file['swap']['attributes'][path_symbol][index])


def get_token_amount(ele, map_file, path_amount):

    tokens_amounts = map_file['swap']['attributes'][path_amount]

    if not(isinstance(tokens_amounts[0], list)):
        return tokens_amounts[0]

    tokens_amounts = [
        dict_digger.dig(
            ele,
            *map_file['swap']['attributes'][path_amount][0]),
        dict_digger.dig(
            ele,
            *map_file['swap']['attributes'][path_amount][1])
    ]

    index = 0
    if(float(tokens_amounts[1]) > 0):
        index = 1

    return tokens_amounts[index]
