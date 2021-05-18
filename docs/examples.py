from deficrawler import Oracle
from deficrawler import Dex
from deficrawler import Lending

# Lending protocols
aave = Lending(protocol="Aave", chain="Ethereum", version=2)
aave_polygon = Lending(protocol="Aave", chain="Polygon", version=2)
compound = Lending(protocol="Compound", chain="Ethereum", version=2)
cream = Lending(protocol="Cream", chain="Ethereum", version=2)
cream_bsc = Lending(protocol="Cream", chain="bsc", version=2)


# Supported entities for aave
print(aave.supported_entities())

# Get borrows in a time period
start_date = '21/04/2021 00:00:01'
end_date = '24/04/2021 23:59:00'


list_borrows = [*aave.get_data_from_date_range(start_date, end_date, "borrow"),
                *aave_polygon.get_data_from_date_range(start_date, end_date, "borrow"),
                *compound.get_data_from_date_range(start_date, end_date, "borrow"),
                *cream_bsc.get_data_from_date_range(start_date, end_date, "borrow"),
                *cream.get_data_from_date_range(start_date, end_date, "borrow")]


print(list_borrows)


# AMM protocols
uniswap = Dex(protocol="Uniswap", chain="Ethereum", version=2)
balancer = Dex(protocol="Balancer", chain="Ethereum", version=1)
bancor = Dex("Bancor", chain="Ethereum", version=1)
shushi = Dex("SushiSwap", chain="Ethereum", version=1)


# Get all the swaps in a time range
start_date_amm = '10/05/2021 00:00:00'
end_date_amm = '10/05/2021 02:00:00'

list_swaps = [*uniswap.get_data_from_date_range(start_date_amm, end_date_amm, "swap"),
              *balancer.get_data_from_date_range(start_date_amm, end_date_amm, "swap"),
              *bancor.get_data_from_date_range(start_date_amm, end_date_amm, "swap"),
              *shushi.get_data_from_date_range(start_date_amm, end_date_amm, "swap")]


print(list_swaps)

# Oracles
chainlink = Oracle(protocol="chainlink", version=1, chain="Ethereum")

# Get the ETH/USD price of a period
start_date = '10/04/2021 00:00:01'
end_date = '10/05/2021 23:59:00'
price_eth = chainlink.get_price_from_date_range(
    from_date=start_date, to_date=end_date, pair="ETH/USD")

print(price_eth)
