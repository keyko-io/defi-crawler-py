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

def test_redeem_aave_2_eth_user():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    redeems = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '31/08/2021 18:01:00', "redeem", "0x27239549dd40e1d60f5b80b0c4196923745b1fd2")

    for redeem in redeems:
        assert(redeem['user'] ==
               "0x27239549dd40e1d60f5b80b0c4196923745b1fd2")


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

def test_redeem_aave_2_polygon_user():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    redeems = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '31/08/2021 02:01:00', "redeem", "0x3fcd5de6a9fc8a99995c406c77dda3ed7e406f81")

    for redeem in redeems:
        assert(redeem['user'] ==
               "0x3fcd5de6a9fc8a99995c406c77dda3ed7e406f81")

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

def test_redeem_compound_2_eth_user():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    redeems = compound.get_data_from_date_range(
        '28/07/2021 00:00:01', '3/07/2021 18:01:00', "redeem", "0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5")

    for redeem in redeems:
        assert(redeem['user'] ==
               "0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5")


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

def test_redeem_cream_2_polygon():
    cream = Lending(protocol="Cream", chain="Polygon", version=2)
    redeem = cream.get_data_from_date_range(
        '25/09/2021 00:00:01', '26/09/2021 18:01:00', "redeem")

    assert(redeem[0]['tx_id'] != "")
    assert(redeem[0]['protocol'] == "Cream")
    assert(redeem[0]['chain'] == "Polygon")
    assert(redeem[0]['version'] == 2)
    assert(redeem[0]['user'] != "")
    assert(redeem[0]['token'] != "")
    assert(float(redeem[0]['amount']) > 0)
    assert(redeem[0]['timestamp'] > 0)



def test_redeem_cream_2_arbitrum():
    cream = Lending(protocol="Cream", chain="Arbitrum", version=2)
    redeem = cream.get_data_from_date_range(
        '25/09/2021 00:00:01', '26/09/2021 18:01:00', "redeem")

    assert(redeem[0]['tx_id'] != "")
    assert(redeem[0]['protocol'] == "Cream")
    assert(redeem[0]['chain'] == "Arbitrum")
    assert(redeem[0]['version'] == 2)
    assert(redeem[0]['user'] != "")
    assert(redeem[0]['token'] != "")
    assert(float(redeem[0]['amount']) > 0)
    assert(redeem[0]['timestamp'] > 0)



def test_redeem_cream_2_eth_user():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    redeems = cream.get_data_from_date_range(
        '28/07/2021 00:00:01', '30/07/2021 18:01:00', "redeem","0x85759961b116f1d36fd697855c57a6ae40793d9b")

    for redeem in redeems:
        assert(redeem['user'] ==
               "0x85759961b116f1d36fd697855c57a6ae40793d9b")


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



def test_redeem_cream_2_bsc_user():
    cream = Lending(protocol="Cream", chain="Bsc", version=2)
    redeems = cream.get_data_from_date_range(
        '28/07/2021 00:00:01', '30/07/2021 18:01:00', "redeem","0x1ffe17b99b439be0afc831239ddecda2a790ff3a")

    for redeem in redeems:
        assert(redeem['user'] ==
               "0x1ffe17b99b439be0afc831239ddecda2a790ff3a")



def test_redeem_kashi_1_eth():
    kashi = Lending(protocol="Kashi", chain="Ethereum", version=1)
    redeem = kashi.get_data_from_date_range(
        '25/09/2021 00:00:01', '30/09/2021 18:01:00', "redeem")

    assert(redeem[0]['tx_id'] != "")
    assert(redeem[0]['protocol'] == "Kashi")
    assert(redeem[0]['chain'] == "Ethereum")
    assert(redeem[0]['version'] == 1)
    assert(redeem[0]['user'] != "")
    assert(redeem[0]['token'] != "")
    assert(float(redeem[0]['amount']) > 0)
    assert(redeem[0]['timestamp'] > 0)


def test_redeem_kashi_1_polygon():
    kashi = Lending(protocol="Kashi", chain="Polygon", version=1)
    redeem = kashi.get_data_from_date_range(
        '25/09/2021 00:00:01', '30/09/2021 18:01:00', "redeem")

    assert(redeem[0]['tx_id'] != "")
    assert(redeem[0]['protocol'] == "Kashi")
    assert(redeem[0]['chain'] == "Polygon")
    assert(redeem[0]['version'] == 1)
    assert(redeem[0]['user'] != "")
    assert(redeem[0]['token'] != "")
    assert(float(redeem[0]['amount']) > 0)
    assert(redeem[0]['timestamp'] > 0)

