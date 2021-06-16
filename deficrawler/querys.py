class Querys:
    QUERY_FROM_TIMESTAMP = """{{
                {entity_name}(
                            first: 1000
                            orderBy: {order_by}
                            orderDirection: asc
                            where: {{
                                {order_by}_gt: {from_timestamp}
                                {order_by}_lte: {to_timestamp}
                                {aditional_filters}
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

    QUERY_FIRST_ELEMENT = """ {{
            {entity_name}(
                    orderBy: {order_by}
                    orderDirection: desc
                    first: 1
                    {block}
                    where: {{
                        {order_by_filter}{lte} {timestamp}
                        {aditional_filters}
                    }}
                ){{
                    {attributes}
                }}
            }}
        """
