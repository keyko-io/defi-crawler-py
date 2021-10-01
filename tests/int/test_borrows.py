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


def test_borrow_aave_2_eth_user():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    borrows = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '12/05/2021 00:01:00', "borrow", "0x8b8cdf85e4378894310e8ec6878d0ca09f105429")

    for borrow in borrows:
        assert(borrow['user'] == "0x8b8cdf85e4378894310e8ec6878d0ca09f105429")


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


def test_borrow_aave_2_polygon_user():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    borrows = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '12/05/2021 00:01:10', "borrow", "0x1fd51540eb1609f58499bddef0b3c345d5d92e3c")

    for borrow in borrows:
        assert(borrow['user'] == "0x1fd51540eb1609f58499bddef0b3c345d5d92e3c")


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


def test_borrow_compound_2_eth_user():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    borrows = compound.get_data_from_date_range(
        '11/05/2021 00:00:01', '14/05/2021 00:01:10', "borrow", "0x162a7cec46225fb915dfd384ae049025dfcf4c10")

    for borrow in borrows:
        assert(borrow['user'] == "0x162a7cec46225fb915dfd384ae049025dfcf4c10")


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


def test_borrow_cream_2_polygon():
    cream = Lending(protocol="Cream", chain="Polygon", version=2)
    borrows = cream.get_data_from_date_range(
        '23/09/2021 00:00:01', '24/09/2021 11:54:10', "borrow")

    assert(borrows[0]['tx_id'] != "")
    assert(borrows[0]['protocol'] == "Cream")
    assert(borrows[0]['chain'] == "Polygon")
    assert(borrows[0]['version'] == 2)
    assert(borrows[0]['user'] != "")
    assert(borrows[0]['token'] != "")
    assert(float(borrows[0]['amount']) > 0)
    assert(borrows[0]['timestamp'] > 0)

def test_borrow_cream_2_arbitrum():
    cream = Lending(protocol="Cream", chain="Arbitrum", version=2)
    borrows = cream.get_data_from_date_range(
        '23/09/2021 00:00:01', '25/09/2021 11:54:10', "borrow")

    assert(borrows[0]['tx_id'] != "")
    assert(borrows[0]['protocol'] == "Cream")
    assert(borrows[0]['chain'] == "Arbitrum")
    assert(borrows[0]['version'] == 2)
    assert(borrows[0]['user'] != "")
    assert(borrows[0]['token'] != "")
    assert(float(borrows[0]['amount']) > 0)
    assert(borrows[0]['timestamp'] > 0)


def test_borrow_cream_2_eth_user():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    borrows = cream.get_data_from_date_range(
        '11/05/2021 00:00:01', '14/05/2021 11:54:10', "borrow", "0x1a32b5993f42e3df3e37cbce3cf270d44a91a960")

    for borrow in borrows:
        assert(borrow['user'] == "0x1a32b5993f42e3df3e37cbce3cf270d44a91a960")


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


def test_borrow_cream_2_bsc_user():
    cream = Lending(protocol="Cream", chain="bsc", version=2)
    borrows = cream.get_data_from_date_range(
        '08/05/2021 00:00:01', '14/05/2021 11:54:10', "borrow", "0x8a8aaaefbeee3fc7ca30a0f9a2c5c5ea0e83ebb0")

    for borrow in borrows:
        assert(borrow['user'] == "0x8a8aaaefbeee3fc7ca30a0f9a2c5c5ea0e83ebb0")



def test_borrow_kashi_1_eth():
    kashi = Lending(protocol="Kashi", chain="Ethereum", version=1)
    borrows = kashi.get_data_from_date_range(
        '30/09/2021 00:00:01', '30/09/2021 11:54:10', "borrow")

    assert(borrows[0]['tx_id'] != "")
    assert(borrows[0]['protocol'] == "Kashi")
    assert(borrows[0]['chain'] == "Ethereum")
    assert(borrows[0]['version'] == 1)
    assert(borrows[0]['user'] != "")
    assert(borrows[0]['token'] != "")
    assert(float(borrows[0]['amount']) > 0)
    assert(borrows[0]['timestamp'] > 0)


def test_borrow_kashi_1_eth_user():
    kashi = Lending(protocol="Kashi", chain="Ethereum", version=1)
    borrows = kashi.get_data_from_date_range(
        '20/09/2021 00:00:01', '30/09/2021 11:54:10', "borrow", "0xb715606b0482bd0ec5c54e8dc616e1deb59d5308")

    for borrow in borrows:
        assert(borrow['user'] == "0xb715606b0482bd0ec5c54e8dc616e1deb59d5308")


def test_borrow_kashi_1_polygon():
    kashi = Lending(protocol="Kashi", chain="Polygon", version=1)
    borrows = kashi.get_data_from_date_range(
        '30/09/2021 00:00:01', '30/09/2021 11:54:10', "borrow")

    assert(borrows[0]['tx_id'] != "")
    assert(borrows[0]['protocol'] == "Kashi")
    assert(borrows[0]['chain'] == "Polygon")
    assert(borrows[0]['version'] == 1)
    assert(borrows[0]['user'] != "")
    assert(borrows[0]['token'] != "")
    assert(float(borrows[0]['amount']) > 0)
    assert(borrows[0]['timestamp'] > 0)
