# Automated markets makers

This document describes the different entities that can be retrieved from the amms protocols

## Swap

Field | Description | Type
--------|-------|--------------
Transaction id | Transaction id of the swap | String
User | User that executed the swap | String
From Token | Token symbol of swap origin | String
To Token | Token symbol of swap destination | String
From Token Amount | Token amount of swap origin | Decimal
To Token Amount | Token amount of swap destination | String
Timestamp | Timestamp of deposit | Timestamp

## Pool

Field | Description | Type
--------|-------|--------------
Id | Unique identifier for pool | String
Liquidity | Total liquidity of the pool | Decimal
Volume | Total volume of the pool | Decimal
Fee | Swap fee of poll | Decimal