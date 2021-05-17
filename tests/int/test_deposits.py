from deficrawler.lending import Lending


def test_deposit_aave_2_eth():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    deposits = aave.get_data_from_date_range(
        '10/05/2021 00:00:01', '11/05/2021 00:01:00', "deposit")
    assert(deposits[0]['tx_id'] != "")
    assert(deposits[0]['protocol'] == "Aave")
    assert(deposits[0]['chain'] == "Ethereum")
    assert(deposits[0]['version'] == 2)
    assert(deposits[0]['user'] != "")
    assert(deposits[0]['token'] != "")
    assert(deposits[0]['amount'] > 0)
    assert(deposits[0]['timestamp'] > 0)


def test_deposit_aave_2_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    deposits = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:10', "deposit")

    assert(deposits[0]['tx_id'] != "")
    assert(deposits[0]['protocol'] == "Aave")
    assert(deposits[0]['chain'] == "Polygon")
    assert(deposits[0]['version'] == 2)
    assert(deposits[0]['user'] != "")
    assert(deposits[0]['token'] != "")
    assert(deposits[0]['amount'] > 0)
    assert(deposits[0]['timestamp'] > 0)


def test_deposit_compound_2_eth():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    deposits = compound.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:10', "deposit")

    assert(deposits[0]['tx_id'] != "")
    assert(deposits[0]['protocol'] == "Compound")
    assert(deposits[0]['chain'] == "Ethereum")
    assert(deposits[0]['version'] == 2)
    assert(deposits[0]['user'] != "")
    assert(deposits[0]['token'] != "")
    assert(float(deposits[0]['amount']) > 0)
    assert(deposits[0]['timestamp'] > 0)


def test_deposit_cream_2_eth():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    deposits = cream.get_data_from_date_range(
        '11/05/2021 00:00:01', '12/05/2021 11:54:10', "deposit")

    assert(deposits[0]['tx_id'] != "")
    assert(deposits[0]['protocol'] == "Cream")
    assert(deposits[0]['chain'] == "Ethereum")
    assert(deposits[0]['version'] == 2)
    assert(deposits[0]['user'] != "")
    assert(deposits[0]['token'] != "")
    assert(float(deposits[0]['amount']) > 0)
    assert(deposits[0]['timestamp'] > 0)


def test_deposit_cream_2_bsc():
    cream = Lending(protocol="Cream", chain="bsc", version=2)
    deposits = cream.get_data_from_date_range(
        '08/05/2021 00:00:01', '12/05/2021 11:54:10', "deposit")

    assert(deposits[0]['tx_id'] != "")
    assert(deposits[0]['protocol'] == "Cream")
    assert(deposits[0]['chain'] == "bsc")
    assert(deposits[0]['version'] == 2)
    assert(deposits[0]['user'] != "")
    assert(deposits[0]['token'] != "")
    assert(float(deposits[0]['amount']) > 0)
    assert(deposits[0]['timestamp'] > 0)
