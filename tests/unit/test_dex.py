from deficrawler.dex import Dex


def test_protocol_entities():
    uniswap = Dex(protocol="Uniswap", chain="Ethereum", version=2)
    balancer = Dex(protocol="Balancer", chain="Ethereum", version=1)

    assert(uniswap.supported_entities() == [
           'swap', 'pool'])
    assert(balancer.supported_entities() == [
        'swap', 'pool'])
