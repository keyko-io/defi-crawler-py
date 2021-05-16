from deficrawler.lending import Lending


def test_protocol_entities():
    aave = Lending(protocol="Aave", chain="Ethereum", version=2)
    compound = Lending(protocol="Compound", chain="Ethereum", version=2)

    assert(aave.supported_entities() == [
           'borrow', 'deposit', 'liquidation', 'repay'])
    assert(compound.supported_entities() == [
          'borrow', 'deposit', 'liquidation', 'repay'])
