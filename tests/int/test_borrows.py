from deficrawler.lending import Lending


def test_borrow_aave_2_eth():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    borrows = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:00', "borrow")
    assert(borrows[0]['tx_id'] != "")
    assert(borrows[0]['protocol'] == "Aave")
    assert(borrows[0]['chain'] == "Ethereum")
    assert(borrows[0]['version'] == 2)
    assert(borrows[0]['user'] != "")
    assert(borrows[0]['token'] != "")
    assert(borrows[0]['amount'] > 0)
    assert(borrows[0]['timestamp'] > 0)


def test_borrow_aave_2_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    borrows = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:10', "borrow")

    assert(borrows[0]['tx_id'] != "")
    assert(borrows[0]['protocol'] == "Aave")
    assert(borrows[0]['chain'] == "Polygon")
    assert(borrows[0]['version'] == 2)
    assert(borrows[0]['user'] != "")
    assert(borrows[0]['token'] != "")
    assert(borrows[0]['amount'] > 0)
    assert(borrows[0]['timestamp'] > 0)


def test_borrow_compound_2_eth():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    borrows = compound.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:10', "borrow")

    assert(borrows[0]['tx_id'] != "")
    assert(borrows[0]['protocol'] == "Compound")
    assert(borrows[0]['chain'] == "Ethereum")
    assert(borrows[0]['version'] == 2)
    assert(borrows[0]['user'] != "")
    assert(borrows[0]['token'] != "")
    assert(float(borrows[0]['amount']) > 0)
    assert(borrows[0]['timestamp'] > 0)


def test_borrow_cream_2_eth():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    borrows = cream.get_data_from_date_range(
        '11/05/2021 00:00:01', '12/05/2021 11:54:10', "borrow")

    assert(borrows[0]['tx_id'] != "")
    assert(borrows[0]['protocol'] == "Cream")
    assert(borrows[0]['chain'] == "Ethereum")
    assert(borrows[0]['version'] == 2)
    assert(borrows[0]['user'] != "")
    assert(borrows[0]['token'] != "")
    assert(float(borrows[0]['amount']) > 0)
    assert(borrows[0]['timestamp'] > 0)


def test_borrow_cream_2_bsc():
    cream = Lending(protocol="Cream", chain="bsc", version=2)
    borrows = cream.get_data_from_date_range(
        '08/05/2021 00:00:01', '12/05/2021 11:54:10', "borrow")

    assert(borrows[0]['tx_id'] != "")
    assert(borrows[0]['protocol'] == "Cream")
    assert(borrows[0]['chain'] == "bsc")
    assert(borrows[0]['version'] == 2)
    assert(borrows[0]['user'] != "")
    assert(borrows[0]['token'] != "")
    assert(float(borrows[0]['amount']) > 0)
    assert(borrows[0]['timestamp'] > 0)
