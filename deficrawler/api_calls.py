from deficrawler.utils import get_attributes, get_filters, filter_method

import requests
import json


def get_data_from(query_input, entity, from_timestamp, to_timestamp, mappings_file, endpoint, aditional_filters=""):
    """
    Gets all the existing data from the subgraph at the given time range.
    One or mor filters can be passed as parameters and will be applied in the where clause
    """
    are_data = True
    json_records = []
    iteration_timestamp = from_timestamp

    entity_name = mappings_file['entities'][entity]['query']['name']
    order_by = mappings_file['entities'][entity]['query']['params']['orderBy']
    attributes = get_attributes(entity, mappings_file)
    filters_str = get_filters(aditional_filters)

    while are_data:
        query = query_input.format(
            entity_name=entity_name,
            order_by=order_by,
            from_timestamp=iteration_timestamp,
            to_timestamp=to_timestamp,
            attributes=attributes,
            aditional_filters=filters_str
        )

        response = requests.post(endpoint, json={'query': query})
        json_data = json.loads(response.text)
        if 'errors' in json_data:
            raise Exception(
                'There was an error getting the data from TheGraph' + json.dumps(json_data))
        else:
            response_lenght = len(json_data['data'][entity_name])
            if (response_lenght > 0):
                json_data = json.loads(response.text)
                list_data = json_data['data'][entity_name]
                iteration_timestamp = json_data['data'][entity_name][response_lenght - 1][order_by]

                json_records = [*json_records, *list_data]
            else:
                are_data = False

    return json_records


def get_data_parameter(query_input, entity, mappings_file, endpoint):
    """
    Gets all the existing data for the given entity.
    If this entity has some filter, in the config file, the query will apply 
    this filter
    """
    are_data = True
    json_records = []

    entity_name = mappings_file['entities'][entity]['query']['name']
    order_by = mappings_file['entities'][entity]['query']['params']['orderBy']
    filter_value = mappings_file['entities'][entity]['query']['params']['initial_value']
    attributes = get_attributes(entity, mappings_file)

    while are_data:
        query = query_input.format(
            entity_name=entity_name,
            order_by=order_by,
            filter_value=filter_value,
            attributes=attributes
        )

        response = requests.post(endpoint, json={'query': query})
        json_data = json.loads(response.text)
        if 'errors' in json_data:
            raise Exception(
                'There was an error getting the data from TheGraph' + json.dumps(json_data))
        else:
            response_lenght = len(json_data['data'][entity_name])
            if (response_lenght > 0):
                json_data = json.loads(response.text)
                list_data = json_data['data'][entity_name]
                filter_value = json_data['data'][entity_name][response_lenght - 1][order_by]

                json_records = [*json_records, *list_data]
            else:
                are_data = False

    return json_records


def get_data_filtered(query_input, entity, mappings_file, endpoint, filters):
    """
    Gets all the existing data from the subgraph applying the given filters
    """
    entity_name = mappings_file['entities'][entity]['query']['name']
    filters_str = get_filters(filters)

    attributes = get_attributes(entity, mappings_file)

    query = query_input.format(
        entity_name=entity_name,
        filters=filters_str,
        attributes=attributes
    )

    response = requests.post(endpoint, json={'query': query})
    json_data = json.loads(response.text)
    json_records = []
    if 'errors' in json_data:
        raise Exception(
            'There was an error getting the data from TheGraph' + json.dumps(json_data))
    else:
        response_lenght = len(json_data['data'][entity_name])
        if (response_lenght > 0):
            json_data = json.loads(response.text)
            list_data = json_data['data'][entity_name]

            json_records = [*list_data]

    return json_records


def get_first_element(query_input, entity, mappings_file, endpoint, timestamp, aditional_filters, block=None):
    """
    Gets first existing data from the subgraph applying the given filters
    """
    entity_name = mappings_file['entities'][entity]['query']['name']
    filters_str = get_filters(aditional_filters)
    order_by = mappings_file['entities'][entity]['query']['params']['orderBy']
    attributes = get_attributes(entity, mappings_file)
    params = filter_method(block=block,
                           order_by_filter=order_by,
                           lte='_lte:',
                           timestamp=timestamp)

    query = query_input.format(
        entity_name=entity_name,
        order_by=order_by,
        order_by_filter=params['order_by_filter'],
        aditional_filters=filters_str,
        attributes=attributes,
        timestamp=params['timestamp'],
        lte=params['lte'],
        block=params['block']
    )

    response = requests.post(endpoint, json={'query': query})
    json_data = json.loads(response.text)
    json_records = []
    if 'errors' in json_data:
        raise Exception(
            'There was an error getting the data from TheGraph' + json.dumps(json_data))
    else:
        response_lenght = len(json_data['data'][entity_name])
        if (response_lenght > 0):
            json_data = json.loads(response.text)
            list_data = json_data['data'][entity_name]

            json_records = [*list_data]

    return json_records
