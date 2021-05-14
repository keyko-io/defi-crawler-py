from deficrawler.transformer import Transformer


def test_no_transformation():
    element = {'id': '0xd522f7c5f29bb6a38d7bbeb08938afb619c8e8a7318a0af0815d4a9d4a8330ac-94',
               'borrower': '0x3f3e305c4ad49271ebda489dd43d2c8f027d2d41',
               'underlyingSymbol': 'USDC', 'amount': '500000', 'blockTime': 1618956398}
    common_field = "user"
    protocol_field = ['borrower']
    transformations = {'tx_id': 'tx_id_hyphen'}
    query_elements = {'tx_id': ['id'], 'user': ['borrower'],
                      'token': ['underlyingSymbol'], 'amount': ['amount'],
                      'timestamp': ['blockTime']}

    transformer = Transformer()

    borrower = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(borrower == '0x3f3e305c4ad49271ebda489dd43d2c8f027d2d41')


def test_decimals():
    element = {'amount': '40000000000', 'id': '0x0fcfca3f64964cd19accad44dbd9e51735cea022224d6cc8aeeed5b418a55f0b:2',
               'reserve': {'decimals': 6, 'symbol': 'USDT'}, 'timestamp': 1618956015,
               'user': {'id': '0x827e2244086565cf8fd7039eb12eb855f56ef167'}}
    common_field = "amount"
    protocol_field = ['amount']
    transformations = {'amount': 'decimals', 'tx_id': 'tx_id_colon'}
    query_elements = {'decimals': ['reserve', 'decimals'], 'tx_id': ['id'], 'user': ['user', 'id'],
                      'token': ['reserve', 'symbol'], 'amount': ['amount'], 'timestamp': ['timestamp']}

    transformer = Transformer()

    decimals = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(decimals == 40000000000 / 10 ** 6)


def test_principal_decimals():
    element = {'collateralAmount': '8390418', 'collateralReserve': {'decimals': 8, 'symbol': 'WBTC'},
               'id': '0x14e3d6aee390617fde0fb893bcc25401bb981d1321242f3010f26da88b16a099:8',
               'liquidator': '0x645e93859ec63abe0c7fe74f17c07c236ee58799', 'principalAmount':
               '1861472948139816454', 'principalReserve': {'decimals': 18, 'symbol': 'WETH'},
               'timestamp': 1618982463, 'user': {'id': '0xcfd873f19a86b84cfc4916e8623f2486dc83d792'}}

    common_field = "amount_principal"
    protocol_field = ['principalAmount']
    transformations = {'amount_principal': 'principal_decimals',
                       'amount_collateral': 'collateral_decimals', 'tx_id': 'tx_id_colon'}
    query_elements = {'principal_decimals': ['principalReserve', 'decimals'],
                      'collateral_decimals': ['collateralReserve', 'decimals'], 'tx_id': ['id'],
                      'user': ['user', 'id'], 'token_principal': ['principalReserve', 'symbol'],
                      'token_collateral': ['collateralReserve', 'symbol'], 'amount_principal': ['principalAmount'],
                      'amount_collateral': ['collateralAmount'], 'liquidator': ['liquidator'], 'timestamp': ['timestamp']}

    transformer = Transformer()

    decimals = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(decimals == 1861472948139816454 / 10 ** 18)


def test_collateral_decimals():
    element = {'collateralAmount': '8390418', 'collateralReserve': {'decimals': 8, 'symbol': 'WBTC'},
               'id': '0x14e3d6aee390617fde0fb893bcc25401bb981d1321242f3010f26da88b16a099:8',
               'liquidator': '0x645e93859ec63abe0c7fe74f17c07c236ee58799', 'principalAmount':
               '1861472948139816454', 'principalReserve': {'decimals': 18, 'symbol': 'WETH'},
               'timestamp': 1618982463, 'user': {'id': '0xcfd873f19a86b84cfc4916e8623f2486dc83d792'}}

    common_field = "amount_collateral"
    protocol_field = ['collateralAmount']
    transformations = {'amount_principal': 'principal_decimals',
                       'amount_collateral': 'collateral_decimals', 'tx_id': 'tx_id_colon'}
    query_elements = {'principal_decimals': ['principalReserve', 'decimals'],
                      'collateral_decimals': ['collateralReserve', 'decimals'], 'tx_id': ['id'],
                      'user': ['user', 'id'], 'token_principal': ['principalReserve', 'symbol'],
                      'token_collateral': ['collateralReserve', 'symbol'], 'amount_principal': ['principalAmount'],
                      'amount_collateral': ['collateralAmount'], 'liquidator': ['liquidator'], 'timestamp': ['timestamp']}

    transformer = Transformer()

    decimals = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(decimals == 8390418 / 10 ** 8)


def test_from_token():
    element = {'amount0In': '0.1', 'amount0Out': '0', 'amount1In': '223212862.542378007',
               'amount1Out': '777931322218.496933182', 'pair': {'token0': {'symbol': 'WETH'}, 'token1': {'symbol': 'HOKK'}},
               'sender': '0x7a250d5630b4cf539739df2c5dacb4c659f2488d',
               'timestamp': '1620079287', 'transaction': {'id': '0xf7bec9d32958801feb1fc06a7dee136e1de844ddbf801ebbb7967b0e39392333'}}

    common_field = "from_token"
    protocol_field = [['pair', 'token0', 'symbol'],
                      ['pair', 'token1', 'symbol']]
    transformations = {'from_token': 'from_token', 'to_token': 'to_token',
                       'from_token_amount': 'from_token_amount', 'to_token_amount': 'to_token_amount'}
    query_elements = {'user': ['sender'], 'tx_id': ['transaction', 'id'], 'from_token': [['pair', 'token0', 'symbol'], ['pair', 'token1', 'symbol']], 'to_token': [['pair', 'token0', 'symbol'], [
        'pair', 'token1', 'symbol']], 'from_token_amount': [['amount0In'], ['amount1In']], 'to_token_amount': [['amount0Out'], ['amount1Out']], 'timestamp': ['timestamp']}

    transformer = Transformer()

    from_token = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(from_token == 'WETH')


def test_to_token():
    element = {'amount0In': '0.1', 'amount0Out': '0', 'amount1In': '223212862.542378007',
               'amount1Out': '777931322218.496933182', 'pair': {'token0': {'symbol': 'WETH'}, 'token1': {'symbol': 'HOKK'}},
               'sender': '0x7a250d5630b4cf539739df2c5dacb4c659f2488d',
               'timestamp': '1620079287', 'transaction': {'id': '0xf7bec9d32958801feb1fc06a7dee136e1de844ddbf801ebbb7967b0e39392333'}}

    common_field = "to_token"
    protocol_field = [['pair', 'token0', 'symbol'],
                      ['pair', 'token1', 'symbol']]
    transformations = {'from_token': 'from_token', 'to_token': 'to_token',
                       'from_token_amount': 'from_token_amount', 'to_token_amount': 'to_token_amount'}
    query_elements = {'user': ['sender'], 'tx_id': ['transaction', 'id'], 'from_token': [['pair', 'token0', 'symbol'], ['pair', 'token1', 'symbol']], 'to_token': [['pair', 'token0', 'symbol'], [
        'pair', 'token1', 'symbol']], 'from_token_amount': [['amount0In'], ['amount1In']], 'to_token_amount': [['amount0Out'], ['amount1Out']], 'timestamp': ['timestamp']}

    transformer = Transformer()

    to_token = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(to_token == 'HOKK')


def test_from_token_amount():
    element = {'amount0In': '0.1', 'amount0Out': '0', 'amount1In': '223212862.542378007',
               'amount1Out': '777931322218.496933182', 'pair': {'token0': {'symbol': 'WETH'}, 'token1': {'symbol': 'HOKK'}},
               'sender': '0x7a250d5630b4cf539739df2c5dacb4c659f2488d',
               'timestamp': '1620079287', 'transaction': {'id': '0xf7bec9d32958801feb1fc06a7dee136e1de844ddbf801ebbb7967b0e39392333'}}

    common_field = "from_token_amount"
    protocol_field = [["amount0In"],
                      ["amount1In"]]
    transformations = {'from_token': 'from_token', 'to_token': 'to_token',
                       'from_token_amount': 'from_token_amount', 'to_token_amount': 'to_token_amount'}
    query_elements = {'user': ['sender'], 'tx_id': ['transaction', 'id'], 'from_token': [['pair', 'token0', 'symbol'], ['pair', 'token1', 'symbol']], 'to_token': [['pair', 'token0', 'symbol'], [
        'pair', 'token1', 'symbol']], 'from_token_amount': [['amount0In'], ['amount1In']], 'to_token_amount': [['amount0Out'], ['amount1Out']], 'timestamp': ['timestamp']}

    transformer = Transformer()

    amount = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(amount == '0.1')


def test_to_token_amount():
    element = {'amount0In': '0.1', 'amount0Out': '0', 'amount1In': '223212862.542378007',
               'amount1Out': '777931322218.496933182', 'pair': {'token0': {'symbol': 'WETH'}, 'token1': {'symbol': 'HOKK'}},
               'sender': '0x7a250d5630b4cf539739df2c5dacb4c659f2488d',
               'timestamp': '1620079287', 'transaction': {'id': '0xf7bec9d32958801feb1fc06a7dee136e1de844ddbf801ebbb7967b0e39392333'}}

    common_field = "to_token_amount"
    protocol_field = [["amount0Out"],
                      ["amount1Out"]]
    transformations = {'from_token': 'from_token', 'to_token': 'to_token',
                       'from_token_amount': 'from_token_amount', 'to_token_amount': 'to_token_amount'}
    query_elements = {'user': ['sender'], 'tx_id': ['transaction', 'id'], 'from_token': [['pair', 'token0', 'symbol'], ['pair', 'token1', 'symbol']], 'to_token': [['pair', 'token0', 'symbol'], [
        'pair', 'token1', 'symbol']], 'from_token_amount': [['amount0In'], ['amount1In']], 'to_token_amount': [['amount0Out'], ['amount1Out']], 'timestamp': ['timestamp']}

    transformer = Transformer()

    amount = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(amount == '777931322218.496933182')


def test_array_length():
    element = {'borrowedReservesCount': 3, 'id': '0x017389d8542b201e4626dde118fd359b972c654d',
               'liquidationCallHistory': [{'id': '0xa81e545027dcde712981a9e32ef071d720fa26d80365d3cccc883726b9a4e00f:8'}]}

    common_field = "liquidations_count"
    protocol_field = ['liquidationCallHistory', 'id']
    transformations = {'liquidations_count': 'array_length'}
    query_elements = {'user_id': ['id'], 'active_loans': [
        'borrowedReservesCount'], 'liquidations_count': ['liquidationCallHistory', 'id']}

    transformer = Transformer()

    liquidations = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(liquidations == 1)


def test_tx_id_colon():
    element = {'collateralAmount': '8390418', 'collateralReserve': {'decimals': 8, 'symbol': 'WBTC'},
               'id': '0x14e3d6aee390617fde0fb893bcc25401bb981d1321242f3010f26da88b16a099:8',
               'liquidator': '0x645e93859ec63abe0c7fe74f17c07c236ee58799', 'principalAmount':
               '1861472948139816454', 'principalReserve': {'decimals': 18, 'symbol': 'WETH'},
               'timestamp': 1618982463, 'user': {'id': '0xcfd873f19a86b84cfc4916e8623f2486dc83d792'}}

    common_field = "tx_id"
    protocol_field = ['id']
    transformations = {'amount_principal': 'principal_decimals',
                       'amount_collateral': 'collateral_decimals', 'tx_id': 'tx_id_colon'}
    query_elements = {'principal_decimals': ['principalReserve', 'decimals'],
                      'collateral_decimals': ['collateralReserve', 'decimals'], 'tx_id': ['id'],
                      'user': ['user', 'id'], 'token_principal': ['principalReserve', 'symbol'],
                      'token_collateral': ['collateralReserve', 'symbol'], 'amount_principal': ['principalAmount'],
                      'amount_collateral': ['collateralAmount'], 'liquidator': ['liquidator'], 'timestamp': ['timestamp']}

    transformer = Transformer()

    tx = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(tx == "0x14e3d6aee390617fde0fb893bcc25401bb981d1321242f3010f26da88b16a099")


def test_tx_id_hyphen():
    element = {'id': '0xd522f7c5f29bb6a38d7bbeb08938afb619c8e8a7318a0af0815d4a9d4a8330ac-94',
               'borrower': '0x3f3e305c4ad49271ebda489dd43d2c8f027d2d41',
               'underlyingSymbol': 'USDC', 'amount': '500000', 'blockTime': 1618956398}
    common_field = "tx_id"
    protocol_field = ['id']
    transformations = {'tx_id': 'tx_id_hyphen'}
    query_elements = {'tx_id': ['id'], 'user': ['borrower'],
                      'token': ['underlyingSymbol'], 'amount': ['amount'],
                      'timestamp': ['blockTime']}

    transformer = Transformer()

    tx_id = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(tx_id == '0xd522f7c5f29bb6a38d7bbeb08938afb619c8e8a7318a0af0815d4a9d4a8330ac')


def test_chainlink_prices():
    element = {'assetPair': {'id': 'ETH/USD'},
               'price': '39178992539', 'timestamp': '1596755816'}
    common_field = "price"
    protocol_field = ['price']
    transformations = {'price': 'chainlink_prices'}
    query_elements = {'pair': ['assetPair', 'id'],
                      'price': ['price'], 'timestamp': ['timestamp']}

    transformer = Transformer()

    price = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(price == 39178992539 / 10 ** 8)

    element = {'assetPair': {'id': 'ENJ/ETH'},
               'price': '513200000000000', 'timestamp': '1596791153'}
    common_field = "price"
    protocol_field = ['price']
    transformations = {'price': 'chainlink_prices'}
    query_elements = {'pair': ['assetPair', 'id'],
                      'price': ['price'], 'timestamp': ['timestamp']}

    transformer = Transformer()

    price = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(price == 513200000000000 / 10 ** 18)


def test_remove_token_prefix():
    element = {'id': '0xe5df2dd6aaca27128fdbba8e22c16198e80d21fe11e7d5309077d313d8c2b9c5-238',
               'to': '0x3c71cf9b6335cf604767d3a07fc19664ce7a9052', 'cTokenSymbol': 'cETH',
               'underlyingAmount': '35', 'blockTime': 1618956266}
    common_field = "token"
    protocol_field = ['cTokenSymbol']
    transformations = {'token': 'remove_token_prefix', 'tx_id': 'tx_id_hyphen'}
    query_elements = {'tx_id': ['id'], 'user': ['to'], 'token': ['cTokenSymbol'],
                      'amount': ['underlyingAmount'], 'timestamp': ['blockTime']}

    transformer = Transformer()

    token = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(token == "ETH")


def test_concat_symbols():
    element = {'amount0In': '0.1', 'amount0Out': '0', 'amount1In': '223212862.542378007',
               'amount1Out': '777931322218.496933182', 'token0': {'symbol': 'WETH'}, 'token1': {'symbol': 'HOKK'},
               'sender': '0x7a250d5630b4cf539739df2c5dacb4c659f2488d',
               'timestamp': '1620079287', 'transaction': {'id': '0xf7bec9d32958801feb1fc06a7dee136e1de844ddbf801ebbb7967b0e39392333'}}

    common_field = "pool_tokens"
    protocol_field = [
        [
            "token0",
            "symbol"
        ],
        [
            "token1",
            "symbol"
        ]
    ]
    transformations = {
        "pool_tokens": "concat_symbols"
    }
    query_elements = {"id": [
        "id"
    ],
        "pool_tokens": [
        [
            "token0",
            "symbol"
        ],
        [
            "token1",
            "symbol"
        ]
    ]}

    transformer = Transformer()

    pool = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(pool == 'WETH/HOKK')


def test_concat_symbols():
    element = {
        "id": "0x00e5a66d31768318a7cae45dd7a0ef8288d7288d",
        "tokens": [
            {
              "symbol": "WBTC"
            },
            {
                "symbol": "DAI"
            },
            {
                "symbol": "USDC"
            },
            {
                "symbol": "WETH"
            },
            {
                "symbol": "renBTC"
            }
        ]
    }

    common_field = "pool_tokens"
    protocol_field = [
        "tokens",
        "symbol"
    ]
    transformations = {
        "pool_tokens": "concat_list_symbols"
    }
    query_elements = {"id": [
        "id"
    ],
        "pool_tokens": [
        "tokens",
        "symbol"
    ]}

    transformer = Transformer()

    pool = transformer.transform(
        element,
        common_field,
        protocol_field,
        transformations,
        query_elements
    )

    assert(pool == 'WBTC/DAI/USDC/WETH/renBTC')
