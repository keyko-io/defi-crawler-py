from deficrawler.lending import Lending


def test_repay_aave_2_eth():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    repays = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:00', "repay")
    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Aave")
    assert(repays[0]['chain'] == "Ethereum")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(repays[0]['amount'] > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_aave_2_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    repays = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Aave")
    assert(repays[0]['chain'] == "Polygon")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(repays[0]['amount'] > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_compound_2_eth():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    repays = compound.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Compound")
    assert(repays[0]['chain'] == "Ethereum")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_cream_2_eth():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    repays = cream.get_data_from_date_range(
        '11/05/2021 00:00:01', '12/05/2021 11:54:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Cream")
    assert(repays[0]['chain'] == "Ethereum")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_cream_2_bsc():
    cream = Lending(protocol="Cream", chain="bsc", version=2)
    repays = cream.get_data_from_date_range(
        '08/05/2021 00:00:01', '12/05/2021 11:54:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Cream")
    assert(repays[0]['chain'] == "bsc")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)
