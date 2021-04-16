# Prices entities

This document describes the different entities that can be retrieved from prices

## Prices feeds

Field | Description | Type
--------|-------|--------------
id | Unique identifier of price feed | String
Asset Pair | Pair of tokens for the price feed | Decimal
Decimals | Number of decimals of the price feed | Decimal

## Price

Field | Description | Type
--------|-------|--------------
Asset Pair | Pair of tokens for the price feed | Decimal
Price | Exchange price of the asset pair | Decimal
Time since last price | Time from the last update of the price feed on the oracle | timestamp
Timestamp | Timestamp of price update | Timestamp

