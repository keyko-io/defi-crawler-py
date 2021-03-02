class Constants:
    PATH_BORROWS = {
        "AAVE": "borrows",
        "COMPOUND": "borrowEvents",
        "MAKER": "vaults",
        "CREAM": "borrowEvents"
    }

    ENDPOINT = {
        "AAVE": "https://api.thegraph.com/subgraphs/name/aave/protocol-v2",
        "COMPOUND": "https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2",
        "MAKER": "https://api.thegraph.com/subgraphs/name/protofire/maker-protocol",
        "CREAM": "https://api.thegraph.com/subgraphs/name/creamfinancedev/cream-lending-v2"
    }

    TIMESTAMP = {
        "AAVE": "timestamp",
        "COMPOUND": "blockTime",
        "MAKER": "openedAt",
        "CREAM": "blockTime"
    }
