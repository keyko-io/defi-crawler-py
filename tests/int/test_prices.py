from deficrawler.lending import Lending


def test_prices_aave_2_eth():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    prices = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '02/05/2022 00:00:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Aave")
    assert(prices[0]['chain'] == "Ethereum")
    assert(prices[0]['version'] == 2)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)

def test_prices_aave_2_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    prices = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '02/05/2022 00:00:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Aave")
    assert(prices[0]['chain'] == "Polygon")
    assert(prices[0]['version'] == 2)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)

def test_prices_aave_2_avalanche():
    aave = Lending(protocol="Aave", chain="Avalanche", version=2)
    prices = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '02/05/2022 00:00:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Aave")
    assert(prices[0]['chain'] == "Avalanche")
    assert(prices[0]['version'] == 2)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)

def test_prices_compound_2_eth():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    prices = compound.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 00:05:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Compound")
    assert(prices[0]['chain'] == "Ethereum")
    assert(prices[0]['version'] == 2)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)

    
def test_prices_cream_2_eth():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    prices = cream.get_data_from_date_range(
        '02/05/2022 00:00:01', '03/05/2022 00:05:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Cream")
    assert(prices[0]['chain'] == "Ethereum")
    assert(prices[0]['version'] == 2)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)


def test_prices_cream_2_bsc():
    cream = Lending(protocol="Cream", chain="Bsc", version=2)
    prices = cream.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 00:05:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Cream")
    assert(prices[0]['chain'] == "Bsc")
    assert(prices[0]['version'] == 2)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)

def test_prices_cream_2_polygon():
    cream = Lending(protocol="Cream", chain="Polygon", version=2)
    prices = cream.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 00:05:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Cream")
    assert(prices[0]['chain'] == "Polygon")
    assert(prices[0]['version'] == 2)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)

def test_prices_cream_2_avalance():
    cream = Lending(protocol="Cream", chain="avalanche", version=2)
    prices = cream.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 00:05:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Cream")
    assert(prices[0]['chain'] == "avalanche")
    assert(prices[0]['version'] == 2)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)


def test_prices_venus_1_bsc():
    compound = Lending(protocol="Venus", chain="Bsc", version=1)
    prices = compound.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 00:05:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Venus")
    assert(prices[0]['chain'] == "Bsc")
    assert(prices[0]['version'] == 1)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)

def test_prices_scream_1_fantom():
    compound = Lending(protocol="Scream", chain="Fantom", version=1)
    prices = compound.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 00:05:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Scream")
    assert(prices[0]['chain'] == "Fantom")
    assert(prices[0]['version'] == 1)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)


def test_prices_aave_3_arbitrum():
    aave = Lending(protocol="Aave", chain="Arbitrum", version=3)
    prices = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 02:00:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Aave")
    assert(prices[0]['chain'] == "Arbitrum")
    assert(prices[0]['version'] == 3)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)


def test_prices_aave_3_optimism():
    aave = Lending(protocol="Aave", chain="optimism", version=3)
    prices = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 02:00:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Aave")
    assert(prices[0]['chain'] == "optimism")
    assert(prices[0]['version'] == 3)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) >= 0)
    assert(float(prices[0]['priceInUsd']) >= 0)
    assert(float(prices[0]['exchangeRate']) >= 0)
    assert(int(prices[0]['timestamp']) > 0)


def test_prices_aave_3_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=3)
    prices = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 02:00:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Aave")
    assert(prices[0]['chain'] == "Polygon")
    assert(prices[0]['version'] == 3)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)

def test_prices_aave_3_fantom():
    aave = Lending(protocol="Aave", chain="fantom", version=3)
    prices = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 02:00:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Aave")
    assert(prices[0]['chain'] == "fantom")
    assert(prices[0]['version'] == 3)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)

def test_prices_aave_3_avalanche():
    aave = Lending(protocol="Aave", chain="Avalanche", version=3)
    prices = aave.get_data_from_date_range(
        '01/05/2022 00:00:01', '01/05/2022 02:00:00', "prices")
    assert(prices[0]['id'] != "")
    assert(prices[0]['protocol'] == "Aave")
    assert(prices[0]['chain'] == "Avalanche")
    assert(prices[0]['version'] == 3)
    assert(prices[0]['symbol'] != "")
    assert(prices[0]['underlyingAsset'] != "")
    assert(float(prices[0]['priceInETH']) > 0)
    assert(float(prices[0]['priceInUsd']) > 0)
    assert(float(prices[0]['exchangeRate']) > 0)
    assert(int(prices[0]['timestamp']) > 0)