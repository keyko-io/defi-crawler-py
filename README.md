[![banner](https://raw.githubusercontent.com/keyko-io/assets/master/images/logo/small/keyko_logo@2x-100.jpg)](https://keyko.io)

# DeFi Crawler Python library
> [keyko.io](https://keyko.io)
---

## Table of Contents

  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Quick-start](#quick-start)
     - [Usage](#usage)
     - [Supported protocols](#supported-protocols)
     - [Testing](#testing)
  - [Contributions](#contributions)
  - [License](#license)

---

## Features

This library allows to get DeFi data from several protocols in a structured and standard way. This data comes from different subgraphs displayed in The Graph protocol

## Prerequisites

Python 3.6

## Quick-start

```
pip install deficrawler
```

### Usage

To get data from a protocol, it's needed to create an instance of the protocol with the name, version and blockchain where the protocols exists, the supported protocols can be found in [supported protocols](#supported-protocols) section. And the entities for the protocols with the field types in the [entities](#https://github.com/keyko-io/defi-crawler-py/tree/main/docs/entities) folder

To get data from Lending protocols

```python
# Instanciate the protocol with the name, version and chain
from deficrawler import Lending

aave = Lending(protocol="Aave", chain="Ethereum", version=2)
aave_polygon = Lending(protocol="Aave", chain="Polygon", version=2)
compound = Lending(protocol="Compound", chain="Ethereum", version=2)
cream = Lending(protocol="Cream", chain="Ethereum", version=2)
cream_bsc = Lending(protocol="Cream", chain="bsc", version=2)

# Not all the protocols has the same available events to get data, to know which entities are supported for each protocol:
aave.supported_entities()
uniswap.suported_entities()

## For each different entity, data can be retrieved in a specific time range.
compound.get_data_from_date_range(start_date, end_date, "borrow")

# To get the all the users of a protocol
cream_bsc.get_all_users()

# And the user positions 
cream_bsc.get_all_users(user)

```

To get data from Dex protocols

```python
# Instanciate the protocol with the name, version and chain
from deficrawler import Dex

uniswap = Dex(protocol="Uniswap", chain="Ethereum", version=2)
balancer = Dex(protocol="Balancer", chain="Ethereum", version=1)
bancor = Dex("Bancor", chain="Ethereum", version=1)
shushi = Dex("SushiSwap", chain="Ethereum", version=1)

# Not all the protocols has the same available events to get data, to know which entities are supported for each protocol:
uniswap.supported_entities()
balancer.suported_entities()

## For each different entity, data can be retrieved in a specific time range.
uniswap.get_data_from_date_range(start_date_amm, end_date_amm, "swap")

# To get the all the pools of a protocol
uniswap.get_all_pools()

```

To get prices from the oracles it's needed to instanciate an oracle object and call the functions.

```python
# Instanciate the oracle with the name, version and chain
from deficrawler import Oracle

chainlink = Oracle(protocol="chainlink", version=1, chain="Ethereum")

#Get all the available pairs to get the data
chainlink.get_all_pairs() 

#Get the price for a specific pair in a time range
chainlink.get_price_from_date_range(from_date=start_date, to_date=end_date, pair="ETH/USD")

```

### Supported-protocols

#### Protocols

Name | Type | Version | Chain
--------|-------|---------|-------
Aave | Lending | 2 | Ethereum
Aave | Lending | 2 | Polygon
Compound | Lending | 2 | Ethereum
Cream | Lending | 2 | Ethereum
Cream | Lending | 2 | BSC
Uniswap | Dexes | 2 | Ethereum
Balancer | Dexes | 2 | Ethereum
Bancor | Dexes | 1 | Ethereum
SushiSwap | Dexes | 1 | Ethereum
SushiSwap | Dexes | 1 | BSC
SushiSwap | Dexes | 1 | Polygon
Ubeswap | Dexes | 1 | Celo


#### Oracles
Name | Type | Version | Chain
--------|-------|---------|-------
Chainlink | Oracle | 1 | Ethereum

#### Testing

Tests are creatd using Pytest library. To run the tests
    
    pytest -v 


#### Examples

To run the examples run 
    
    python3 docs/examples.py 


### Contributions
If you want to add a new protocol to be supported or a new entity to retrive data, create a PR with the new configuration of the protocol and the unit/integration tests of this new feature.

To add a new protocol, create a new json config file in the config folder, with the struture `protocolname-version.json`.
Inside this configuration file must be the following sections:
##### Protocol
This section specifies the global configuration of the protocol. The required fields are 
  - **Name:** Protocol name.
  - **Type:** Protocol type (Borrowing lending)
  - **Version:** Version of the protcol
  - **Enpoint:** Subgrapn endpoint to send the http request to get the data. If the protocols exists on more than one chain, several enpoints can be provided
 
**Example**
````json
  "protocol": {
    "name": "AAVE",
    "type": "Lending",
    "version": 2,
    "endpoint": {
      "ethereum": "https://api.thegraph.com/subgraphs/name/aave/protocol-v2",
      "polygon": "https://api.thegraph.com/subgraphs/name/aave/aave-v2-matic"
    }
  }
````

  
After this section the supported entities should be specified. Each entity has three different sections inside of them.
  - **Entity:** The entity contains the fields to create a common entity from a shared type of event of different protocols (borrow, swap, deposit...). The entity starts with the name that will be applied to this specific event across all the protocols. Then should be a field for each attribute that will be contained in the entity, and each field shoud have an array, with the path to find this element in the corresponding subpgraph, these fields will be used to create the query. As example for borrow entity in Aave:
    ````
    "borrow": {
      "attributes": {
        "tx_id":[
          "id"
        ],
        "user": [
          "user",
          "id"
        ],
        "token": [
          "reserve",
          "symbol"
        ],
        "amount": [
          "amount"
        ],
        "timestamp": [
          "timestamp"
        ]
      }
  - **Query:**: Each query in each protocol can be named different, to allow create the query dynamically, the query name should be specified and the field to order by if will be more that one batch to retrive. In this section also can be specified, additional fields to get data from the subgraph that will be needed to apply transformations, but will not be part of the output itself. As example for Aave we need to get the decimals for the token to divide the amount, but the decimals are not part of the entity. As example
      ````
          "query": {
            "extra_fields": {
              "decimals": [
                "reserve",
                "decimals"
              ]
            },
            "name": "borrows",
            "params": {
              "orderBy": "timestamp"
            }
          }
  - **Tranformations:** This section specified the transformations that should be applied to the fields (if any transformation should be applied). Here we can specify the field of the common entity (the output) that needs to be transform, and the function that will be applied. This funtion will be call dinamically in the transformation phase. As example:
      ````
          "transformations": {
            "amount": "decimals",
            "tx_id":"tx_id_colon"
          }
      ````
    
## License

```text
Copyright 2020 Keyko GmbH.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
