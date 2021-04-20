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

    USERS = {
        "AAVE": """
                {{
                users(
                    first: 1000
                    orderBy: id
                    orderDirection: asc
                    where: {{
                    id_gt: "{}"
                    }}
                ){{
                    id
                    borrowedReservesCount
                    liquidationCallHistory{{
                        id
                    }}
                }}
            }}
        """
    }

    USERS_POSITIONS = {
        "AAVE": """
                {{
                userReserves(
                 where: {{
                    user:"{}"
                }}
            ){{
                user{{
                    id
                }}
                reserve{{
                    symbol
                }}
                currentTotalDebt
                currentATokenBalance
            }}
            }}
        """
    }
