from deficrawler.lending import Lending


def test_repay_aave_2_eth():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    repays = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:31:00', "repay")
    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Aave")
    assert(repays[0]['chain'] == "Ethereum")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(repays[0]['amount'] > 0)
    assert(repays[0]['timestamp'] > 0)

def test_repay_aave_2_eth_user():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    repays = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:00', "repay", "0xe1d18ae098ffb1ad301e0609180f155b329a710a")

    for repay in repays:
        assert(repay['user'] ==
               "0xe1d18ae098ffb1ad301e0609180f155b329a710a")


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


def test_repay_aave_2_avalanche():
    aave = Lending(protocol="Aave", chain="Avalanche", version=2)
    repays = aave.get_data_from_date_range(
        '17/10/2021 00:00:01', '18/10/2021 00:01:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Aave")
    assert(repays[0]['chain'] == "Avalanche")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(repays[0]['amount'] > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_aave_2_polygon_user():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    repays = aave.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:10', "repay", "0x88b71294c66cbcb077a4626921fd8b8df6ecf042")

    for repay in repays:
        assert(repay['user'] ==
               "0x88b71294c66cbcb077a4626921fd8b8df6ecf042")


def test_repay_compound_2_eth():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    repays = compound.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:31:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Compound")
    assert(repays[0]['chain'] == "Ethereum")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)

def test_repay_compound_2_eth_user():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    repays = compound.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:01:10', "repay", "0x5fec8b5630fb7b923d9308902856054996829f60")

    for repay in repays:
        assert(repay['user'] ==
               "0x5fec8b5630fb7b923d9308902856054996829f60")

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


def test_repay_cream_2_arbitrum():
    cream = Lending(protocol="Cream", chain="Arbitrum", version=2)
    repays = cream.get_data_from_date_range(
        '20/09/2021 00:00:01', '26/09/2021 11:54:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Cream")
    assert(repays[0]['chain'] == "Arbitrum")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)

def test_repay_cream_2_polygon():
    cream = Lending(protocol="Cream", chain="Polygon", version=2)
    repays = cream.get_data_from_date_range(
        '25/09/2021 00:00:01', '26/09/2021 11:54:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Cream")
    assert(repays[0]['chain'] == "Polygon")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)

def test_repay_cream_2_eth_user():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    repays = cream.get_data_from_date_range(
        '11/05/2021 00:00:01', '12/05/2021 11:54:10', "repay", "0xf662eba33a8630b51a3d955213dd7a58c2a687a9")

    for repay in repays:
        assert(repay['user'] ==
               "0xf662eba33a8630b51a3d955213dd7a58c2a687a9")

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



def test_repay_cream_2_bsc():
    cream = Lending(protocol="Cream", chain="avalanche", version=2)
    repays = cream.get_data_from_date_range(
        '18/10/2021 00:00:01', '19/10/2021 00:00:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Cream")
    assert(repays[0]['chain'] == "avalanche")
    assert(repays[0]['version'] == 2)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_cream_2_bsc():
    cream = Lending(protocol="Cream", chain="bsc", version=2)
    repays = cream.get_data_from_date_range(
        '08/05/2021 00:00:01', '12/05/2021 11:54:10', "repay", "0x86caaf4e8592cbe7f93a8ccec1c4be6b61be7693")

    for repay in repays:
        assert(repay['user'] ==
               "0x86caaf4e8592cbe7f93a8ccec1c4be6b61be7693")


def test_repay_kashi_1_eth():
    kashi = Lending(protocol="Kashi", chain="Ethereum", version=1)
    repays = kashi.get_data_from_date_range(
        '20/09/2021 00:00:01', '20/09/2021 11:54:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Kashi")
    assert(repays[0]['chain'] == "Ethereum")
    assert(repays[0]['version'] == 1)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_venus_1_bsc():
    compound = Lending(protocol="Venus", chain="Bsc", version=1)
    repays = compound.get_data_from_date_range(
        '11/05/2021 00:00:01', '11/05/2021 00:31:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Venus")
    assert(repays[0]['chain'] == "Bsc")
    assert(repays[0]['version'] == 1)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_scream_1_fantom():
    compound = Lending(protocol="Scream", chain="fantom", version=1)
    repays = compound.get_data_from_date_range(
        '10/05/2022 00:00:01', '11/05/2022 00:31:10', "repay")

    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Scream")
    assert(repays[0]['chain'] == "fantom")
    assert(repays[0]['version'] == 1)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(float(repays[0]['amount']) > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_aave_3_arbitrum():
    aave = Lending(protocol="Aave", chain="Arbitrum", version=3)
    repays = aave.get_data_from_date_range(
        '11/05/2022 00:00:01', '11/05/2022 22:31:00', "repay")
    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Aave")
    assert(repays[0]['chain'] == "Arbitrum")
    assert(repays[0]['version'] == 3)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(repays[0]['amount'] > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_aave_3_optimism():
    aave = Lending(protocol="Aave", chain="Optimism", version=3)
    repays = aave.get_data_from_date_range(
        '11/05/2022 00:00:01', '11/05/2022 22:31:00', "repay")
    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Aave")
    assert(repays[0]['chain'] == "Optimism")
    assert(repays[0]['version'] == 3)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(repays[0]['amount'] > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_aave_3_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=3)
    repays = aave.get_data_from_date_range(
        '11/05/2022 00:00:01', '11/05/2022 22:31:00', "repay")
    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Aave")
    assert(repays[0]['chain'] == "Polygon")
    assert(repays[0]['version'] == 3)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(repays[0]['amount'] > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_aave_3_fantom():
    aave = Lending(protocol="Aave", chain="Fantom", version=3)
    repays = aave.get_data_from_date_range(
        '11/05/2022 00:00:01', '11/05/2022 22:31:00', "repay")
    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Aave")
    assert(repays[0]['chain'] == "Fantom")
    assert(repays[0]['version'] == 3)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(repays[0]['amount'] > 0)
    assert(repays[0]['timestamp'] > 0)


def test_repay_aave_3_avalanche():
    aave = Lending(protocol="Aave", chain="Avalanche", version=3)
    repays = aave.get_data_from_date_range(
        '11/05/2022 00:00:01', '11/05/2022 22:31:00', "repay")
    assert(repays[0]['tx_id'] != "")
    assert(repays[0]['protocol'] == "Aave")
    assert(repays[0]['chain'] == "Avalanche")
    assert(repays[0]['version'] == 3)
    assert(repays[0]['user'] != "")
    assert(repays[0]['token'] != "")
    assert(repays[0]['amount'] > 0)
    assert(repays[0]['timestamp'] > 0)