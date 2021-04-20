def get_attributes(event, map_file):
    list_attr = ''
    attributes = map_file[event]['attributes']
    for attribute, value in attributes.items():
        list_attr += format_attribute(value) + " "
    return list_attr

def format_attribute(list_fields):
    if(len(list_fields) == 1):
        return list_fields[0]

    path = list_fields[0] + '{'
    for index, field in enumerate(list_fields):
        if index > 0:
            path += field
    path += '}'
    return path

