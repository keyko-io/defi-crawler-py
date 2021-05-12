from deficrawler.protocol_base import ProtocolBase

import pytest


def test_protocol_not_exits():
    with pytest.raises(Exception) as execinfo:
        ProtocolBase(protocol="NA", version=12, chain="other")

    assert execinfo.value.args[0] == 'Protocol NA version 12 not supported'


def test_enpoint_not_exits():
    with pytest.raises(Exception) as execinfo:
        ProtocolBase(protocol="Aave", version=2, chain="other")

    assert execinfo.value.args[0] == 'Protocol Aave chain other not supported'


def test_entity_not_exits():
    with pytest.raises(Exception) as execinfo:
        protocol = ProtocolBase(protocol="Compound", version=2, chain="Ethereum")
        protocol.get_protocol_config('swap')

    assert execinfo.value.args[0] == 'Entity swap not supported for protocol Compound'
    

def test_protocol_exits():
    protocol = ProtocolBase(protocol="Compound", version=2, chain="Ethereum")
    config = protocol.get_protocol_config('borrow')
    assert('attributes' in config)
    assert('transformations' in config)
    assert('query_elements' in config)





