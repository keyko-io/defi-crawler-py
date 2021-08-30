from deficrawler.lending import Lending


def test_flashloans_aave_2_eth():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    flash_loans = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '30/08/2021 18:01:00', "flashloans")

    print(flash_loans)
    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Ethereum")
    assert(flash_loans[0]['version'] == 2)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)


def test_flashloans_aave_2_polygon():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    flash_loans = aave.get_data_from_date_range(
        '30/08/2021 00:00:01', '30/08/2021 18:01:00', "flashloans")
    assert(flash_loans[0]['tx_id'] != "")
    assert(flash_loans[0]['protocol'] == "Aave")
    assert(flash_loans[0]['chain'] == "Polygon")
    assert(flash_loans[0]['version'] == 2)
    assert(flash_loans[0]['user'] != "")
    assert(flash_loans[0]['token'] != "")
    assert(flash_loans[0]['amount'] > 0)
    assert(flash_loans[0]['timestamp'] > 0)