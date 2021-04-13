# Lending protocols

This document describes the different entities that can be retrieved from the lending protocols

## Deposits

Field | Description | Type
--------|-------|--------------
User | User | String
Amount | Amount of token deposited | Decimal
Token | Token symbol of deposit | String
Timestamp | Timestamp of deposit | Timestamp

## Borrows

Field | Description | Type
--------|-------|--------------
User | User | String
Amount | Amount of token deposited | Decimal
Token | Token symbol of borrow | String
Timestamp | Timestamp of borrow | Timestamp

## Repay

Field | Description | Type
--------|-------|--------------
User | User | String
Amount | Amount of token repaid | Decimal
Token | Token symbol of repaid | String
Timestamp | Timestamp of repaid | Timestamp

## Liquidation

Field | Description | Type
--------|-------|--------------
User | User | String
Principal Token | Token payed on liquidation to repay debt | Decimal
Collateral Token | Token received by liquidator on liquidation | String
Principal Amount | Amount of principal payed on liquidation | Timestamp
Collateral Amount | Amount of collateral recevided by liquidator | Decimal
Liquidator | Address of the liquidator | String
Timestamp | Timestamp of liquidation | Timestamp

## User

Field | Description | Type
--------|-------|--------------
User id | User | String
Active loans | Number of loans that the user has currently open | Integer
Liquidations Count | Number of liquidations received by the user | Integer

## User positions

Field | Description | Type
--------|-------|--------------
User | User | String
Symbol | Symbol of the token in the user portfolio | String
Debt amount | Amount of debt tokens | Decimal
Collateral amount | Amount of collateral tokens | Decimal