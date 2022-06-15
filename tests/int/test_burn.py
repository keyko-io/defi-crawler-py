from deficrawler.dex import Dex


def test_burn_uniswap_2_eth():
    uniswap = Dex(protocol="Uniswap", chain="Ethereum", version=2)
    burns = uniswap.get_data_from_date_range(
        '04/05/2021 00:00:00', '04/05/2021 00:10:30', "burn")

    assert(burns[0]['tx_id'] != "")
    assert(burns[0]['protocol'] == "Uniswap")
    assert(burns[0]['chain'] == "Ethereum")
    assert(burns[0]['version'] == 2)
    assert(burns[0]['user'] != "")
    assert(burns[0]['token0'] != "")
    assert(burns[0]['token1'] != "")
    assert(burns[0]['pool'] != "")
    assert(float(burns[0]['amount0']) > 0)
    assert(float(burns[0]['amount1']) > 0)
    assert(float(burns[0]['timestamp']) > 0)


def test_burn_uniswap_3_eth():
    uniswap = Dex(protocol="Uniswap", chain="Ethereum", version=3)
    burns = uniswap.get_data_from_date_range(
        '30/09/2021 00:00:00', '30/09/2021 02:00:30', "burn")

    assert(burns[0]['tx_id'] != "")
    assert(burns[0]['protocol'] == "Uniswap")
    assert(burns[0]['chain'] == "Ethereum")
    assert(burns[0]['version'] == 3)
    assert(burns[0]['user'] != "")
    assert(burns[0]['token0'] != "")
    assert(burns[0]['token1'] != "")
    assert(burns[0]['pool'] != "")
    assert(float(burns[0]['amount0']) > 0)
    assert(float(burns[0]['amount1']) >= 0)
    assert(float(burns[0]['timestamp']) > 0)



# def test_burn_ubeswap_2_celo():
    # ubeswap = Dex(protocol="Ubeswap", chain="Celo", version=1)
    # burns = ubeswap.get_data_from_date_range(
    #     '30/09/2021 00:00:00', '30/09/2021 01:00:30', "burn")

    # assert(burns[0]['tx_id'] != "")
    # assert(burns[0]['protocol'] == "Ubeswap")
    # assert(burns[0]['chain'] == "Celo")
    # assert(burns[0]['version'] == 1)
    # assert(burns[0]['user'] != "")
    # assert(burns[0]['token0'] != "")
    # assert(burns[0]['token1'] != "")
    # assert(burns[0]['pool'] != "")
    # assert(float(burns[0]['amount0']) > 0)
    # assert(float(burns[0]['amount1']) > 0)
    # assert(float(burns[0]['timestamp']) > 0)


def test_burn_sushi_2_eth():
    sushi = Dex(protocol="Sushiswap", chain="Ethereum", version=1)
    burns = sushi.get_data_from_date_range(
        '30/09/2021 00:00:00', '30/09/2021 01:00:30', "burn")

    assert(burns[0]['tx_id'] != "")
    assert(burns[0]['protocol'] == "Sushiswap")
    assert(burns[0]['chain'] == "Ethereum")
    assert(burns[0]['version'] == 1)
    assert(burns[0]['user'] != "")
    assert(burns[0]['token0'] != "")
    assert(burns[0]['token1'] != "")
    assert(burns[0]['pool'] != "")
    assert(float(burns[0]['amount0']) > 0)
    assert(float(burns[0]['amount1']) > 0)
    assert(float(burns[0]['timestamp']) > 0)

def test_burn_sushi_2_bsc():
    sushi = Dex(protocol="Sushiswap", chain="bsc", version=1)
    burns = sushi.get_data_from_date_range(
        '30/09/2021 00:00:00', '30/09/2021 02:00:30', "burn")

    assert(burns[0]['tx_id'] != "")
    assert(burns[0]['protocol'] == "Sushiswap")
    assert(burns[0]['chain'] == "bsc")
    assert(burns[0]['version'] == 1)
    assert(burns[0]['user'] != "")
    assert(burns[0]['token0'] != "")
    assert(burns[0]['token1'] != "")
    assert(burns[0]['pool'] != "")
    assert(float(burns[0]['amount0']) > 0)
    assert(float(burns[0]['amount1']) > 0)
    assert(float(burns[0]['timestamp']) > 0)


def test_burn_sushi_2_polygon():
    sushi = Dex(protocol="Sushiswap", chain="polygon", version=1)
    burns = sushi.get_data_from_date_range(
        '30/09/2021 00:00:00', '30/09/2021 01:00:30', "burn")

    assert(burns[0]['tx_id'] != "")
    assert(burns[0]['protocol'] == "Sushiswap")
    assert(burns[0]['chain'] == "polygon")
    assert(burns[0]['version'] == 1)
    assert(burns[0]['user'] != "")
    assert(burns[0]['token0'] != "")
    assert(burns[0]['token1'] != "")
    assert(burns[0]['pool'] != "")
    assert(float(burns[0]['amount0']) > 0)
    assert(float(burns[0]['amount1']) > 0)
    assert(float(burns[0]['timestamp']) > 0)

def test_burn_sushi_2_fantom():
    sushi = Dex(protocol="Sushiswap", chain="fantom", version=1)
    burns = sushi.get_data_from_date_range(
        '30/09/2021 00:00:00', '30/09/2021 09:00:30', "burn")

    assert(burns[0]['tx_id'] != "")
    assert(burns[0]['protocol'] == "Sushiswap")
    assert(burns[0]['chain'] == "fantom")
    assert(burns[0]['version'] == 1)
    assert(burns[0]['user'] != "")
    assert(burns[0]['token0'] != "")
    assert(burns[0]['token1'] != "")
    assert(burns[0]['pool'] != "")
    assert(float(burns[0]['amount0']) > 0)
    assert(float(burns[0]['amount1']) > 0)
    assert(float(burns[0]['timestamp']) > 0)


def test_burn_sushi_1_celo():
    sushi = Dex(protocol="Sushiswap", chain="celo", version=1)
    burns = sushi.get_data_from_date_range(
        '17/10/2021 00:00:00', '17/10/2021 03:00:30', "burn")

    assert(burns[0]['tx_id'] != "")
    assert(burns[0]['protocol'] == "Sushiswap")
    assert(burns[0]['chain'] == "celo")
    assert(burns[0]['version'] == 1)
    assert(burns[0]['user'] != "")
    assert(burns[0]['token0'] != "")
    assert(burns[0]['token1'] != "")
    assert(burns[0]['pool'] != "")
    assert(float(burns[0]['amount0']) > 0)
    assert(float(burns[0]['amount1']) > 0)
    assert(float(burns[0]['timestamp']) > 0)


def test_burn_quickswap_1_polygon():
    quickswap = Dex(protocol="quickswap", chain="polygon", version=1)
    burns = quickswap.get_data_from_date_range(
        '30/09/2021 00:00:00', '30/09/2021 01:00:30', "burn")

    assert(burns[0]['tx_id'] != "")
    assert(burns[0]['protocol'] == "quickswap")
    assert(burns[0]['chain'] == "polygon")
    assert(burns[0]['version'] == 1)
    assert(burns[0]['user'] != "")
    assert(burns[0]['token0'] != "")
    assert(burns[0]['token1'] != "")
    assert(burns[0]['pool'] != "")
    assert(float(burns[0]['amount0']) > 0)
    assert(float(burns[0]['amount1']) > 0)
    assert(float(burns[0]['timestamp']) > 0)



def test_burn_pangolin_1_avalanche():
    pangolin = Dex(protocol="pangolin", chain="avalanche", version=1)
    mints = pangolin.get_data_from_date_range(
        '30/09/2021 00:00:00', '30/09/2021 01:00:30', "burn")

    assert(mints[0]['tx_id'] != "")
    assert(mints[0]['protocol'] == "pangolin")
    assert(mints[0]['chain'] == "avalanche")
    assert(mints[0]['version'] == 1)
    assert(mints[0]['user'] != "")
    assert(mints[0]['token0'] != "")
    assert(mints[0]['token1'] != "")
    assert(mints[0]['pool'] != "")
    assert(float(mints[0]['amount0']) > 0)
    assert(float(mints[0]['amount1']) > 0)
    assert(float(mints[0]['timestamp']) > 0)
