from deficrawler.utils import format_attribute, format_element, get_attributes, get_filters

import pkgutil
import json


def test_get_filters():
    filters_empty = get_filters('')
    assert(filters_empty == '')

    one_filter = get_filters({"user": "account"})
    assert(one_filter == "user:\"account\"\n")

    several_filtes = get_filters({"user": "account", "pair": "assetPair"})
    assert(several_filtes == "user:\"account\"\npair:\"assetPair\"\n")


def test_format_element():
    one_element = ["id"]
    one_formatted = format_element(one_element)
    assert(one_formatted == "id")

    two_elements = ["user", "id"]
    two_formatted = format_element(two_elements)
    assert(two_formatted == "user{id}")

    three_elements = ["pair", "token", "symbol"]
    three_formatted = format_element(three_elements)
    assert(three_formatted == "pair{token{symbol}}")


def test_format_attribute():
    one_attribute = ["sender"]
    one_formatted = format_attribute(one_attribute)
    assert(one_formatted == "sender")

    two_attribute = [
        [
            "pair",
            "token0",
            "symbol"
        ],
        [
            "pair",
            "token1",
            "symbol"
        ]
    ]

    two_formatted = format_attribute(two_attribute)
    assert(two_formatted == "pair{token0{symbol}} pair{token1{symbol}} ")


def test_get_attributes():
    config_file = pkgutil.get_data(
        'deficrawler.config',
        'aave' + "-" + str('2') + ".json"
    )

    map_file = json.loads(config_file.decode())
    borrow_attr = get_attributes('borrow', map_file)
    print(borrow_attr == "reserve{decimals} id user{id} reserve{symbol} amount timestamp ")

    config_file = pkgutil.get_data(
        'deficrawler.config',
        'uniswap' + "-" + str('2') + ".json"
    )

    map_file = json.loads(config_file.decode())
    swap_attr = get_attributes('swap', map_file)
    assert(swap_attr =="sender transaction{id} pair{token0{symbol}} pair{token1{symbol}}  pair{token0{symbol}} pair{token1{symbol}}  amount0In amount1In  amount0Out amount1Out  timestamp ")

