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


def test_deposit_aave_2_eth_user():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    deposits = aave.get_data_from_date_range(
        '10/05/2021 00:00:01', '14/05/2021 00:01:00', "deposit", "0x63a3f444e97d14e671e7ee323c4234c8095e3516")

    for deposit in deposits:
        assert(deposit['user'] == "0x63a3f444e97d14e671e7ee323c4234c8095e3516")


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


def test_deposit_aave_2_polygon_user():
    aave = Lending(protocol="Aave", chain="Polygon", version=2)
    deposits = aave.get_data_from_date_range(
        '10/05/2021 00:00:01', '12/05/2021 00:01:00', "deposit", "0xbeadf48d62acc944a06eeae0a9054a90e5a7dc97")

    for deposit in deposits:
        assert(deposit['user'] == "0xbeadf48d62acc944a06eeae0a9054a90e5a7dc97")


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


def test_deposit_compound_2_eth_user():
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)
    deposits = compound.get_data_from_date_range(
        '11/05/2021 00:00:01', '14/05/2021 00:01:10', "deposit", "0x862e840c2f7edd2c709d8de0df71c03210ed5267")

    for deposit in deposits:
        assert(deposit['user'] == "0x862e840c2f7edd2c709d8de0df71c03210ed5267")


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

def test_deposit_cream_2_polygon():
    cream = Lending(protocol="Cream", chain="Polygon", version=2)
    deposits = cream.get_data_from_date_range(
        '25/09/2021 00:00:01', '26/09/2021 11:54:10', "deposit")

    assert(deposits[0]['tx_id'] != "")
    assert(deposits[0]['protocol'] == "Cream")
    assert(deposits[0]['chain'] == "Polygon")
    assert(deposits[0]['version'] == 2)
    assert(deposits[0]['user'] != "")
    assert(deposits[0]['token'] != "")
    assert(float(deposits[0]['amount']) > 0)
    assert(deposits[0]['timestamp'] > 0)



def test_deposit_cream_2_eth_user():
    cream = Lending(protocol="Cream", chain="Ethereum", version=2)
    deposits = cream.get_data_from_date_range(
        '11/05/2021 00:00:01', '14/05/2021 11:54:10', "deposit", "0xe6a6ee4196d361ec4f6d587c7ebe20c50667fb39")

    for deposit in deposits:
        assert(deposit['user'] == "0xe6a6ee4196d361ec4f6d587c7ebe20c50667fb39")


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


def test_deposit_cream_2_bsc_user():
    cream = Lending(protocol="Cream", chain="bsc", version=2)
    deposits = cream.get_data_from_date_range(
        '08/05/2021 00:00:01', '14/05/2021 11:54:10', "deposit", "0xc6fb91e0ee3b1077c5465d54b3dda176a695199b")

    for deposit in deposits:
        assert(deposit['user'] == "0xc6fb91e0ee3b1077c5465d54b3dda176a695199b")


def test_deposit_kashi_1_eth():
    kashi = Lending(protocol="kashi", chain="Ethereum", version=1)
    deposits = kashi.get_data_from_date_range(
        '25/09/2021 00:00:01', '30/09/2021 11:54:10', "deposit")

    assert(deposits[0]['tx_id'] != "")
    assert(deposits[0]['protocol'] == "kashi")
    assert(deposits[0]['chain'] == "Ethereum")
    assert(deposits[0]['version'] == 1)
    assert(deposits[0]['user'] != "")
    assert(deposits[0]['token'] != "")
    assert(float(deposits[0]['amount']) > 0)
    assert(deposits[0]['timestamp'] > 0)


def test_deposit_kashi_1_polygon():
    kashi = Lending(protocol="kashi", chain="Polygon", version=1)
    deposits = kashi.get_data_from_date_range(
        '25/09/2021 00:00:01', '30/09/2021 11:54:10', "deposit")

    assert(deposits[0]['tx_id'] != "")
    assert(deposits[0]['protocol'] == "kashi")
    assert(deposits[0]['chain'] == "Polygon")
    assert(deposits[0]['version'] == 1)
    assert(deposits[0]['user'] != "")
    assert(deposits[0]['token'] != "")
    assert(float(deposits[0]['amount']) > 0)
    assert(deposits[0]['timestamp'] > 0)
