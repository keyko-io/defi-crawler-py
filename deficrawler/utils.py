def get_attributes(entity, map_file):
    list_attr = ''
    attributes = map_file['entities'][entity]['query']['fields']
    for attribute, value in attributes.items():
        list_attr += format_attribute(value) + " "
    return list_attr


def get_filters(params, filter_dict):
    filters = ''

    for filter_name, filter_value in filter_dict.items():
        filters += params[filter_name] + ":\"" + filter_value + "\"\n"

    return filters


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
