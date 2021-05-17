from deficrawler.lending import Lending

def test_liquidation_aave_2_eth():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    liquidations = aave.get_data_from_date_range(
        '21/04/2021 05:20:01', '22/04/2021 06:22:01', "liquidation")
    assert(liquidations[0]['tx_id'] != "")
    assert(liquidations[0]['protocol'] == "Aave")
    assert(liquidations[0]['chain'] == "Ethereum")
    assert(liquidations[0]['version'] == 2)
    assert(liquidations[0]['user'] != "")
    assert(liquidations[0]['token_principal'] != "")
    assert(liquidations[0]['token_collateral'] != "")
    assert(liquidations[0]['amount_principal'] > 0)
    assert(liquidations[0]['amount_collateral'] > 0)
    assert(liquidations[0]['liquidator'] != "")
    assert(liquidations[0]['timestamp'] > 0)


def test_liquidation_aave_2_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    liquidations = aave.get_data_from_date_range(
        '10/05/2021 00:00:01', '11/05/2021 00:01:10', "liquidation")

    assert(liquidations[0]['tx_id'] != "")
    assert(liquidations[0]['protocol'] == "Aave")
    assert(liquidations[0]['chain'] == "Polygon")
    assert(liquidations[0]['version'] == 2)
    assert(liquidations[0]['user'] != "")
    assert(liquidations[0]['token_principal'] != "")
    assert(liquidations[0]['token_collateral'] != "")
    assert(liquidations[0]['amount_principal'] > 0)
    assert(liquidations[0]['amount_collateral'] > 0)
    assert(liquidations[0]['liquidator'] != "")
    assert(liquidations[0]['timestamp'] > 0)


def test_liquidation_compound_2_eth():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    liquidations = compound.get_data_from_date_range(
        '09/05/2021 00:00:01', '11/05/2021 00:01:10', "liquidation")

    assert(liquidations[0]['tx_id'] != "")
    assert(liquidations[0]['protocol'] == "Compound")
    assert(liquidations[0]['chain'] == "Ethereum")
    assert(liquidations[0]['version'] == 2)
    assert(liquidations[0]['user'] != "")
    assert(liquidations[0]['token_principal'] != "")
    assert(liquidations[0]['token_collateral'] != "")
    assert(float(liquidations[0]['amount_principal']) > 0)
    assert(float(liquidations[0]['amount_collateral']) > 0)
    assert(liquidations[0]['liquidator'] != "")
    assert(liquidations[0]['timestamp'] > 0)


def test_liquidation_cream_2_eth():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    liquidations = cream.get_data_from_date_range(
        '01/05/2021 00:00:01', '12/05/2021 11:54:10', "liquidation")

    assert(liquidations[0]['tx_id'] != "")
    assert(liquidations[0]['protocol'] == "Cream")
    assert(liquidations[0]['chain'] == "Ethereum")
    assert(liquidations[0]['version'] == 2)
    assert(liquidations[0]['user'] != "")
    assert(liquidations[0]['token_principal'] != "")
    assert(liquidations[0]['token_collateral'] != "")
    assert(float(liquidations[0]['amount_principal']) > 0)
    assert(float(liquidations[0]['amount_collateral']) > 0)
    assert(liquidations[0]['liquidator'] != "")
    assert(liquidations[0]['timestamp'] > 0)


def test_liquidation_cream_2_bsc():
    cream = Lending(protocol="Cream", chain="bsc", version=2)
    liquidations = cream.get_data_from_date_range(
        '01/05/2021 00:00:01', '12/05/2021 11:54:10', "liquidation")

    assert(liquidations[0]['tx_id'] != "")
    assert(liquidations[0]['protocol'] == "Cream")
    assert(liquidations[0]['chain'] == "bsc")
    assert(liquidations[0]['version'] == 2)
    assert(liquidations[0]['user'] != "")
    assert(liquidations[0]['token_principal'] != "")
    assert(liquidations[0]['token_collateral'] != "")
    assert(float(liquidations[0]['amount_principal']) > 0)
    assert(float(liquidations[0]['amount_collateral']) > 0)
    assert(liquidations[0]['liquidator'] != "")
    assert(liquidations[0]['timestamp'] > 0)
