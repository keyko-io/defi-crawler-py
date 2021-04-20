from deficrawler.utils import get_attributes

import requests
import json
import pkgutil



def get_data_from(query_input, event, from_timestamp, to_timestamp, protocol):
    are_data = True
    json_records = []
    iteration_timestamp = from_timestamp

    protocol_file = pkgutil.get_data('deficrawler.config', protocol.lower() + ".json")
    map_file = json.loads(protocol_file.decode())

    event_name = map_file[event]['query']['name']
    order_by = map_file[event]['query']['params']['orderBy']
    attributes = get_attributes(event, map_file)

    while are_data:
        query = query_input.format(
            event_name=event_name,
            order_by=order_by,
            from_timestamp=iteration_timestamp,
            to_timestamp=to_timestamp,
            attributes=attributes
        )

        response = requests.post(map_file['endpoint'], json={'query': query})
        json_data = json.loads(response.text)
        if 'errors' in json_data:
            are_data = False
        else:
            response_lenght = len(json_data['data'][event_name])
            if (response_lenght > 0):
                json_data = json.loads(response.text)
                list_data = json_data['data'][event_name]
                iteration_timestamp = json_data['data'][event_name][response_lenght - 1][order_by]

                json_records = [*json_records, *list_data]
            else:
                are_data = False

    return json_records


def get_all_data(query_input, endpoint, path, order_by, order_by_name):
    are_data = True
    json_records = []
    iteration_order_by = order_by

    while are_data:
        query = query_input.format(iteration_order_by)
        response = requests.post(endpoint, json={'query': query})
        json_data = json.loads(response.text)
        if 'errors' in json_data:
            are_data = False
            print(json_data)
        else:
            response_lenght = len(json_data['data'][path])
            if (response_lenght > 0):
                json_data = json.loads(response.text)
                list_data = json_data['data'][path]
                iteration_order_by = json_data['data'][path][response_lenght -
                                                             1][order_by_name]

                json_records = [*json_records, *list_data]
            else:
                are_data = False

    return json_records


def get_data_parameter(query_input, endpoint, path, parameter):
    json_records = []

    query = query_input.format(str(parameter).lower())
    response = requests.post(endpoint, json={'query': query})
    json_data = json.loads(response.text)
    if 'errors' in json_data:
        print(json_data)
    else:
        response_lenght = len(json_data['data'][path])
        if (response_lenght > 0):
            json_data = json.loads(response.text)
            list_data = json_data['data'][path]

    return list_data
