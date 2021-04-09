class Constants:
    PATH_BORROWS = {
        "AAVE": "borrows",
        "COMPOUND": "borrowEvents",
        "MAKER": "vaults",
        "CREAM": "borrowEvents"
    }

    PATH_DEPOSITS = {
        "AAVE": "deposits",
        "COMPOUND": "mintEvents",
        "MAKER": "vaults",
        "CREAM": "mintEvents"
    }

    PATH_LIQUIDATIONS = {
        "AAVE": "liquidationCalls",
        "COMPOUND": "liquidationEvents",
        "MAKER": "vaults",
        "CREAM": "liquidationEvents"
    }

    PATH_REPAYS = {
        "AAVE": "repays",
        "COMPOUND": "repayEvents",
        "MAKER": "vaults",
        "CREAM": "repayEvents"
    }

    PATH_SWAPS = {
        "UNISWAP": "swaps",
        "BALANCER": "swaps",
        "BANCOR": "swaps",
        "SUSHISWAP": "swaps",
        "KYBER": "fullTrades"
    }

    PATH_USERS_ORDER = {
        "AAVE": "id"
    }

    PATH_USERS = {
        "AAVE": "users"
    }

    PATH_POSITIONS = {
        "AAVE": "userReserves"
    }

    ENDPOINT = {
        "AAVE": "https://api.thegraph.com/subgraphs/name/aave/protocol-v2",
        "COMPOUND": "https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2",
        "MAKER": "https://api.thegraph.com/subgraphs/name/protofire/maker-protocol",
        "CREAM": "https://api.thegraph.com/subgraphs/name/creamfinancedev/cream-lending-v2",
        "UNISWAP": "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2",
        "BALANCER": "https://api.thegraph.com/subgraphs/name/balancer-labs/balancer",
        "BANCOR": "https://api.thegraph.com/subgraphs/name/blocklytics/bancor",
        "SUSHISWAP": "https://api.thegraph.com/subgraphs/name/croco-finance/sushiswap",
        "KYBER": "https://api.thegraph.com/subgraphs/name/protofire/kyber"
    }

    TIMESTAMP = {
        "AAVE": "timestamp",
        "COMPOUND": "blockTime",
        "MAKER": "openedAt",
        "CREAM": "blockTime",
        "UNISWAP": "timestamp",
        "BALANCER": "timestamp",
        "BANCOR": "timestamp",
        "SUSHISWAP": "timestamp",
        "KYBER": "createdAtBlockTimestamp"
    }
