class Querys:

    QUERY_FROM_TIMESTAMP = """{{
                {event_name}(
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
