def get_attributes(entity, map_file):
    """
    Returns the list of attributes for the given map file and entity.
    The list is created joining the attributes of the entity and the
    extra fields (if exists) to create the query
    """
    list_attr = ''
    attributes = map_file['entities'][entity]['query']['extra_fields']
    attributes.update(map_file['entities'][entity]['attributes'])
    for attribute, value in attributes.items():
        list_attr += format_attribute(value) + " "
    return list_attr


def get_filters(filter_dict):
    """
    Returns the filters list in string mode for a given dictionary.
    Gets all the filters that the dictionary contains and create a list
    of key:value elements
    """
    filters = ''

    if type(filter_dict) is dict:
        for filter_name, filter_value in filter_dict.items():
            if(filter_name != 'block'):
                filters += filter_name + ":\"" + filter_value + "\"\n"

    return filters


def format_element(list_elements):
    """
    Formats the element to query the subgraph.
    If only one element is given returns the element, in other case
    format the element with the format element{subelement{subsubelement}}
    """
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
    """
    Format the attribute to base on the information of the json file.
    For each field calls the format element, can be a single list wich
    returns a single element or a list of lists that will concatenate the
    strings for each list
    """
    str_list_attr = ""

    if(isinstance(list_fields[0], list)):
        for list_elements in list_fields:
            str_list_attr += format_element(list_elements) + " "
    else:
        str_list_attr += format_element(list_fields)
    return str_list_attr


def block_or_timestamp(order_by_filter, timestamp, aditional_filters):
    """
    Returns the filter type depending of the given filters
    If block is present will be filter by block, in other case
    timestamp
    """
    filters = {}
    if 'block' in aditional_filters:
        filters['order_by_filter'] = ''
        filters['timestamp'] = ''
        filters['lte'] = ""
        filters['block'] = "block: {{number: {block}}}".format(
            block=aditional_filters['block'])
    else:
        filters['order_by_filter'] = order_by_filter
        filters['timestamp'] = timestamp
        filters['lte'] = "_lte:"
        filters['block'] = ''

    return filters
