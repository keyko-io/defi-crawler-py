from deficrawler.dex import Dex


def test_swap_uniswap_2_eth():
    uniswap = Dex(protocol="Uniswap", chain="Ethereum", version=2)
    swaps = uniswap.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 00:00:30', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "Uniswap")
    assert(swaps[0]['chain'] == "Ethereum")
    assert(swaps[0]['version'] == 2)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_balancer_1_eth():
    uniswap = Dex(protocol="Balancer", chain="Ethereum", version=1)
    swaps = uniswap.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 00:01:30', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "Balancer")
    assert(swaps[0]['chain'] == "Ethereum")
    assert(swaps[0]['version'] == 1)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_bancor_1_eth():
    uniswap = Dex(protocol="Bancor", chain="Ethereum", version=1)
    swaps = uniswap.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 04:00:30', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "Bancor")
    assert(swaps[0]['chain'] == "Ethereum")
    assert(swaps[0]['version'] == 1)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_shushi_1_eth():
    shushi = Dex(protocol="SushiSwap", chain="Ethereum", version=1)
    swaps = shushi.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 0:01:30', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "SushiSwap")
    assert(swaps[0]['chain'] == "Ethereum")
    assert(swaps[0]['version'] == 1)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)

    list_swaps = shushi.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 0:01:30', "swap", pool='0xceff51756c56ceffca006cd410b03ffc46dd3a58'
    )

    assert(len(list_swaps) > 0)


def test_swap_shushi_1_bsc():
    shushi = Dex(protocol="SushiSwap", chain="bsc", version=1)
    swaps = shushi.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 0:01:30', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "SushiSwap")
    assert(swaps[0]['chain'] == "bsc")
    assert(swaps[0]['version'] == 1)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_shushi_1_polygon():
    shushi = Dex(protocol="SushiSwap", chain="polygon", version=1)
    swaps = shushi.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 0:01:30', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "SushiSwap")
    assert(swaps[0]['chain'] == "polygon")
    assert(swaps[0]['version'] == 1)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_shushi_1_fantom():
    shushi = Dex(protocol="SushiSwap", chain="fantom", version=1)
    swaps = shushi.get_data_from_date_range(
        '31/08/2021 00:00:00', '31/08/2021 04:00:00', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "SushiSwap")
    assert(swaps[0]['chain'] == "fantom")
    assert(swaps[0]['version'] == 1)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_uniswap_3_eth():
    uniswap = Dex(protocol="Uniswap", chain="Ethereum", version=3)
    swaps = uniswap.get_data_from_date_range(
        '31/08/2021 00:00:00', '31/08/2021 00:10:00', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "Uniswap")
    assert(swaps[0]['chain'] == "Ethereum")
    assert(swaps[0]['version'] == 3)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_ubeswap_1_celo():
    ubeswap = Dex(protocol="ubeswap", chain="celo", version=1)
    swaps = ubeswap.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 0:01:30', "swap")

    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "ubeswap")
    assert(swaps[0]['chain'] == "celo")
    assert(swaps[0]['version'] == 1)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_balancer_2_eth():
    balancer = Dex(protocol="balancer", chain="ethereum", version=2)
    swaps = balancer.get_data_from_date_range(
        '31/08/2021 00:00:00', '31/08/2021 01:00:00', "swap")

    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "balancer")
    assert(swaps[0]['chain'] == "ethereum")
    assert(swaps[0]['version'] == 2)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_balancer_2_polygon():
    balancer = Dex(protocol="balancer", chain="polygon", version=2)
    swaps = balancer.get_data_from_date_range(
        '31/08/2021 00:00:00', '31/08/2021 01:00:00', "swap")

    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "balancer")
    assert(swaps[0]['chain'] == "polygon")
    assert(swaps[0]['version'] == 2)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_balancer_2_arbitrum():
    balancer = Dex(protocol="balancer", chain="arbitrum", version=2)
    swaps = balancer.get_data_from_date_range(
        '31/08/2021 00:00:00', '01/09/2021 0:01:30', "swap")

    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "balancer")
    assert(swaps[0]['chain'] == "arbitrum")
    assert(swaps[0]['version'] == 2)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_pancakeswap_2_bsc():
    pancakeswap = Dex(protocol="pancakeswap", chain="bsc", version=2)
    swaps = pancakeswap.get_data_from_date_range(
        '31/08/2021 00:00:00', '01/09/2021 0:01:30', "swap")

    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "pancakeswap")
    assert(swaps[0]['chain'] == "bsc")
    assert(swaps[0]['version'] == 2)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(swaps[0]['pool'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


