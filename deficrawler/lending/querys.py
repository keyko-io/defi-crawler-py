class Querys:
    BORROWS_FROM_TIMESTAMP = """{{
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
    LIQUIDATIONS_FROM_TIMESTAMP = {
        "AAVE": """{{
                    liquidationCalls(
                            first: 1000
                            orderBy:timestamp
                            orderDirection: asc
                            where: {{
                            timestamp_gt: {}
                            timestamp_lte: {}
                            }}
                        ){{
                            user{{
                                id
                            }}
                            principalReserve{{
                                symbol
                            }}
                            collateralReserve{{
                                symbol
                            }}
                            principalAmount
                            collateralAmount
                            liquidator
                            timestamp
                    }}
                    }}
                """,
        "COMPOUND": """{{
                        liquidationEvents(
                                first: 1000
                                orderBy: blockTime
                                orderDirection:asc
                                where: {{
                                blockTime_gt: {}
                                blockTime_lte: {}
                                }}
                            ){{
                                amount
                                to
                                from
                                blockTime
                                underlyingSymbol
                                underlyingRepayAmount
                                cTokenSymbol
                            }}
                        }}
                """,
        "MAKER": """
                {{
                vaults(
                    first:1000
                    orderBy: openedAt
                    orderDirection:desc
                        where: {{
                            openedAt_gt: {}
                            openedAt_lte: {}
                        }}
                ){{
                    owner{{
                        address
                    }}
                    debt
                    openedAt
                }}
                }}
        """,
        "CREAM": """
            {{
            liquidationEvents(
                first:1000
                orderBy:blockTime
                orderDirection:desc
                where: {{
                blockTime_gt:{}
                blockTime_lte:{}
                }}
            ){{
                amount
                to
                from
                blockTime
                underlyingSymbol
                underlyingRepayAmount
                cTokenSymbol
            }}
            }}
    """
    }

    DEPOSITS_FROM_TIMESTAMP = {
        "AAVE": """
                    {{
                        deposits(
                            first:1000
                            orderBy:timestamp
                            orderDirection:asc
                        where: {{
                            timestamp_gt: {}
                            timestamp_lte: {}
                            }}
                    ){{
                        user{{
                            id
                        }}
                        amount
                        timestamp
                        reserve{{
                        symbol
                        }}
                    }}
                    }}
                """,

        "COMPOUND": """ 
                    {{
                    mintEvents(
                        first:1000
                        orderBy:blockTime
                        orderDirection: asc
                        where: {{
                        blockTime_gt: {}
                        blockTime_lte: {}
                        }}
                    ){{
                        underlyingAmount
                        to
                        cTokenSymbol
                        blockTime
                    }}
                    }}
        """,
        "CREAM": """ 
                    {{
                    mintEvents(
                        first:1000
                        orderBy:blockTime
                        orderDirection: asc
                        where: {{
                        blockTime_gt: {}
                        blockTime_lte: {}
                        }}
                    ){{
                        underlyingAmount
                        to
                        cTokenSymbol
                        blockTime
                    }}
                    }}
        """
    }

    REPAYS_FROM_TIMESTAMP = {
        "AAVE": """
                    {{
                        repays(
                            first:1000
                            orderBy:timestamp
                            orderDirection:asc
                        where: {{
                            timestamp_gt: {}
                            timestamp_lte: {}
                            }}
                    ){{
                        user{{
                            id
                        }}
                        amount
                        timestamp
                        reserve{{
                           symbol
                        }}
                    }}
                    }}
                """,

        "COMPOUND": """ 
                    {{
                    repayEvents(
                        first:1000
                        orderBy:blockTime
                        orderDirection: asc
                        where: {{
                        blockTime_gt: {}
                        blockTime_lte: {}
                        }}
                    ){{
                        payer
                        underlyingSymbol
                        amount
                        blockTime
                    }}
                    }}
        """,
        "CREAM": """ 
                    {{
                    repayEvents(
                        first:1000
                        orderBy:blockTime
                        orderDirection: asc
                        where: {{
                        blockTime_gt: {}
                        blockTime_lte: {}
                        }}
                    ){{
                        payer
                        underlyingSymbol
                        amount
                        blockTime
                    }}
                    }}
        """
    }

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
