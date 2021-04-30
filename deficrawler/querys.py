class Querys:
    QUERY_FROM_TIMESTAMP = """{{
                {entity_name}(
                            first: 1000
                            orderBy: {order_by}
                            orderDirection: asc
                            where: {{
                                {order_by}_gt: {from_timestamp}
                                {order_by}_lte: {to_timestamp}
                            }}
                        ){{
                        {attributes}
                    }}
                    }}
                """

    QUERY_ALL_ELEMENTS = """ {{
            {entity_name}(
                    first: 1000
                    orderBy: {order_by}
                    orderDirection: asc
                    where: {{
                        {order_by}_gt:"{filter_value}"
                    }}
                ){{
                    {attributes}
                }}
            }}
        """

    QUERY_ELEMENT_FILTER = """ {{
            {entity_name}(
                    first: 1000
                    where: {{
                        {filters}
                    }}
                ){{
                    {attributes}
                }}
            }}
        """
