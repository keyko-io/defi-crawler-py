from deficrawler.lending import Lending


def test_redeem_aave_2_eth():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    redeem = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '30/08/2021 18:01:00', "redeem")

    assert(redeem[0]['tx_id'] != "")
    assert(redeem[0]['protocol'] == "Aave")
    assert(redeem[0]['chain'] == "Ethereum")
    assert(redeem[0]['version'] == 2)
    assert(redeem[0]['user'] != "")
    assert(redeem[0]['token'] != "")
    assert(redeem[0]['amount'] > 0)
    assert(redeem[0]['timestamp'] > 0)


def test_redeem_aave_2_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    redeem = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '30/08/2021 02:01:00', "redeem")
    assert(redeem[0]['tx_id'] != "")
    assert(redeem[0]['protocol'] == "Aave")
    assert(redeem[0]['chain'] == "Polygon")
    assert(redeem[0]['version'] == 2)
    assert(redeem[0]['user'] != "")
    assert(redeem[0]['token'] != "")
    assert(redeem[0]['amount'] > 0)
    assert(redeem[0]['timestamp'] > 0)


def test_redeem_compound_2_eth():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    redeem = compound.get_data_from_date_range(
        '28/07/2021 00:00:01', '30/07/2021 18:01:00', "redeem")

    assert(redeem[0]['tx_id'] != "")
    assert(redeem[0]['protocol'] == "Compound")
    assert(redeem[0]['chain'] == "Ethereum")
    assert(redeem[0]['version'] == 2)
    assert(redeem[0]['user'] != "")
    assert(redeem[0]['token'] != "")
    assert(float(redeem[0]['amount']) > 0)
    assert(redeem[0]['timestamp'] > 0)


def test_redeem_cream_2_eth():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    redeem = cream.get_data_from_date_range(
        '28/07/2021 00:00:01', '30/07/2021 18:01:00', "redeem")

    assert(redeem[0]['tx_id'] != "")
    assert(redeem[0]['protocol'] == "Cream")
    assert(redeem[0]['chain'] == "Ethereum")
    assert(redeem[0]['version'] == 2)
    assert(redeem[0]['user'] != "")
    assert(redeem[0]['token'] != "")
    assert(float(redeem[0]['amount']) > 0)
    assert(redeem[0]['timestamp'] > 0)


def test_redeem_cream_2_bsc():
    cream = Lending(protocol="Cream", chain="Bsc", version=2)
    redeem = cream.get_data_from_date_range(
        '28/07/2021 00:00:01', '30/07/2021 18:01:00', "redeem")

    assert(redeem[0]['tx_id'] != "")
    assert(redeem[0]['protocol'] == "Cream")
    assert(redeem[0]['chain'] == "Bsc")
    assert(redeem[0]['version'] == 2)
    assert(redeem[0]['user'] != "")
    assert(redeem[0]['token'] != "")
    assert(float(redeem[0]['amount']) > 0)
    assert(redeem[0]['timestamp'] > 0)
