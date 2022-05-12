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
        '01/05/2022 00:00:01', '01/05/2022 00:05:00', "prices")
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
