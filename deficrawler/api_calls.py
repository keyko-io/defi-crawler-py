import requests
import json


def get_data_from(query_input, endpoint, path, from_timestamp, to_timestamp, timestamp_name):
    are_data = True
    json_records = []
    iteration_timestamp = from_timestamp

    while are_data:
        query = query_input.format(iteration_timestamp, to_timestamp)
        response = requests.post(endpoint, json={'query': query})
        json_data = json.loads(response.text)
        response_lenght = len(json_data['data'][path])
        if (response_lenght > 0):
            json_data = json.loads(response.text)
            list_data = json_data['data'][path]
            iteration_timestamp = json_data['data'][path][response_lenght -
                                                          1][timestamp_name]

            json_records = [*json_records, *list_data]
        else:
            are_data = False

    return json_records
