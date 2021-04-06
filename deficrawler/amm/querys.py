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
                """,
        "BALANCER": """{{
                    swaps(
                        first: 1000
                        orderBy: timestamp
                        orderDirection: asc
                        where: {{
                            timestamp_gt: {}
                            timestamp_lte: {}
                        }}
                    ){{
                        id
                        userAddress{{
                            id
                        }}
                        tokenInSym
                        tokenOutSym
                        tokenAmountIn
                        tokenAmountOut
                        value
                        feeValue
                        timestamp
                    }}
                }}""",
        "BANCOR": """
                    {{
                    swaps(
                        first:1000
                        orderBy:timestamp
                        orderDirection: asc
                        where:{{
                            timestamp_gt: {}
                            timestamp_lte: {}
                        }}
                    ){{
                        id
                        fromToken{{
                            symbol
                        }}
                        toToken{{
                            symbol
                        }}
                        amountPurchased
                        amountReturned
                        price
                        timestamp
                        transaction{{
                            id
                        }}
                        trader{{
                            id
                        }}
                      }}
                    }}
                """,
        "SUSHISWAP": """{{
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
                """,

        "KYBER": """
                   {{
                    fullTrades(
                        first:1000
                        orderBy: createdAtBlockTimestamp
                        orderDirection:asc
                        where: {{
                        createdAtBlockTimestamp_gt: {}
                        createdAtBlockTimestamp_lte: {}
                        }}
                    ) {{
                        id
                        rawSrcAmount
                        rawDestAmount
                        createdAtBlockTimestamp
                        trader {{
                            id
                        }}
                        src {{
                            symbol
                        }}
                        dest {{
                            symbol
                        }}
                     }}
                    }}
                """
    }
