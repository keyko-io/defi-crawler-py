from deficrawler.utils import get_attributes, get_filters

import requests
import json
import pkgutil


def get_data_from(query_input, entity, from_timestamp, to_timestamp, mappings_file, protocol, endpoint):
    are_data = True
    json_records = []
    iteration_timestamp = from_timestamp

    entity_name = mappings_file['entities'][entity]['query']['name']
    order_by = mappings_file['entities'][entity]['query']['params']['orderBy']
    attributes = get_attributes(entity, mappings_file)

    while are_data:
        query = query_input.format(
            entity_name=entity_name,
            order_by=order_by,
            from_timestamp=iteration_timestamp,
            to_timestamp=to_timestamp,
            attributes=attributes
        )

        response = requests.post(endpoint, json={'query': query})
        json_data = json.loads(response.text)
        if 'errors' in json_data:
            are_data = False
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


def get_data_parameter(query_input, entity, mappings_file, protocol, endpoint):
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
            are_data = False
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


def get_data_filtered(query_input, entity, mappings_file, protocol, endpoint, filters):
    entity_name = mappings_file['entities'][entity]['query']['name']
    filters_str = get_filters(
        mappings_file['entities'][entity]['query']['params'], filters)

    attributes = get_attributes(entity, mappings_file)

    query = query_input.format(
        entity_name=entity_name,
        filters=filters_str,
        attributes=attributes
    )

    response = requests.post(endpoint, json={'query': query})
    json_data = json.loads(response.text)
    if 'errors' in json_data:
        are_data = False
    else:
        response_lenght = len(json_data['data'][entity_name])
        if (response_lenght > 0):
            json_data = json.loads(response.text)
            list_data = json_data['data'][entity_name]

            json_records = [*list_data]

    return json_records
