from deficrawler.transformer import Transformer


class Mappers:
    """
    Class to map the data from the subgraph data to the commom model defined in the json file.
    For each field applies the transformaton (if needed) and retuns the entity with all
    the fields.
    """

    @staticmethod
    def map_data(response_data, protocol, chain, version, attributes, transformations, query_elements):
        list_elements = []

        transformer = Transformer()

        for ele in response_data:
            element = {}
            for common_field, protocol_field in attributes.items():
                element[common_field] = (
                    transformer.transform(
                        element=ele,
                        common_field=common_field,
                        protocol_field=protocol_field,
                        transformations=transformations,
                        query_elements=query_elements
                    )
                )
                element['protocol'] = protocol
                element['chain'] = chain
                element['version'] = version
            list_elements.append(element)

        return list_elements
