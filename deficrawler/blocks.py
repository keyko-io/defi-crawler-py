from deficrawler.protocol_base import ProtocolBase

from datetime import datetime


class Block(ProtocolBase):
    """
    Class to get data info for blocks
    """
    def __init__(self, protocol, chain, version):
        super().__init__(
            protocol=protocol,
            chain=chain,
            version=version
        )