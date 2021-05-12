from deficrawler import Protocol


def test_swap_uniswap_2_eth():
    uniswap = Protocol(protocol="Uniswap", chain="Ethereum", version=2)
    swaps = uniswap.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 00:00:30', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "Uniswap")
    assert(swaps[0]['chain'] == "Ethereum")
    assert(swaps[0]['version'] == 2)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_balancer_1_eth():
    uniswap = Protocol(protocol="Balancer", chain="Ethereum", version=1)
    swaps = uniswap.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 00:01:30', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "Balancer")
    assert(swaps[0]['chain'] == "Ethereum")
    assert(swaps[0]['version'] == 1)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


def test_swap_bancor_1_eth():
    uniswap = Protocol(protocol="Bancor", chain="Ethereum", version=1)
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
    uniswap = Protocol(protocol="SushiSwap", chain="Ethereum", version=1)
    swaps = uniswap.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 0:01:30', "swap")
    assert(swaps[0]['tx_id'] != "")
    assert(swaps[0]['protocol'] == "SushiSwap")
    assert(swaps[0]['chain'] == "Ethereum")
    assert(swaps[0]['version'] == 1)
    assert(swaps[0]['user'] != "")
    assert(swaps[0]['from_token'] != "")
    assert(swaps[0]['to_token'] != "")
    assert(float(swaps[0]['from_token_amount']) > 0)
    assert(float(swaps[0]['to_token_amount']) > 0)
    assert(float(swaps[0]['timestamp']) > 0)


