class Querys:
    SWAPS_FROM_TIMESTAMP = {
        "UNISWAP": """{{
                        swaps(
                            orderBy:timestamp
                            orderDirection: asc
                            first:1000
                            where:{{
                                timestamp_gt: {}
                                timestamp_lte: {}
                            }}
                        ){{
                            id
                            sender
                            timestamp
                            amount0Out
                            amount1Out
                            amount0In
                            amount1In
                            transaction{{
                                id
                            }}
                            pair{{
                                token0{{
                                    symbol
                                }}
                                token1{{
                                    symbol
                                }}
                            }}
                        }}
                    }}
                """
    }
