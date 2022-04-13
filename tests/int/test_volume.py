from deficrawler.dex import Dex

def test_volumne_uniswap_2_eth():
    uniswap = Dex(protocol="Uniswap", chain="Ethereum", version=2)
    hourly = uniswap.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "Uniswap")
    assert(hourly[0]['chain'] == "Ethereum")
    assert(hourly[0]['version'] == 2)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) > 0)
    assert(float(hourly[0]['hourlyVolumeUSD']) > 0)
    assert(float(hourly[0]['hourlyVolumeToken0']) > 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) > 0)
    assert(float(hourly[0]['hourlyTxns']) > 0)
    assert(float(hourly[0]['hourStartUnix']) > 0)


def test_volume_pancake_2_bsc():
    pancake = Dex(protocol="Pancakeswap", chain="bsc", version=2)
    hourly = pancake.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='09/03/2022 01:00:00',
        entity='pool_volume_hourly',
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "Pancakeswap")
    assert(hourly[0]['chain'] == "bsc")
    assert(hourly[0]['version'] == 2)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(float(hourly[0]['hourlyVolumeUSD']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)



def test_volume_sushi_1_fantom():
    sushi = Dex(protocol="Sushiswap", chain="fantom", version=1)
    hourly = sushi.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='09/03/2022 01:00:00',
        entity='pool_volume_hourly',
        pool='0x0103715fd20a3f2e11fd7b3e646a5f6f6703d245'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "Sushiswap")
    assert(hourly[0]['chain'] == "fantom")
    assert(hourly[0]['version'] == 1)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(float(hourly[0]['hourlyVolumeUSD']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)


def test_volume_sushi_1_bsc():
    sushi = Dex(protocol="Sushiswap", chain="bsc", version=1)
    hourly = sushi.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "Sushiswap")
    assert(hourly[0]['chain'] == "bsc")
    assert(hourly[0]['version'] == 1)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(float(hourly[0]['hourlyVolumeUSD']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)



def test_volume_sushi_1_eth():
    sushi = Dex(protocol="Sushiswap", chain="ethereum", version=1)
    hourly = sushi.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "Sushiswap")
    assert(hourly[0]['chain'] == "ethereum")
    assert(hourly[0]['version'] == 1)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(float(hourly[0]['hourlyVolumeUSD']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)


def test_volume_sushi_1_polygon():
    sushi = Dex(protocol="Sushiswap", chain="polygon", version=1)
    hourly = sushi.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "Sushiswap")
    assert(hourly[0]['chain'] == "polygon")
    assert(hourly[0]['version'] == 1)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(float(hourly[0]['hourlyVolumeUSD']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)



def test_volume_quickswap_1_polygon():
    quickswap = Dex(protocol="QuickSwap", chain="polygon", version=1)
    hourly = quickswap.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "QuickSwap")
    assert(hourly[0]['chain'] == "polygon")
    assert(hourly[0]['version'] == 1)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(float(hourly[0]['hourlyVolumeUSD']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)



def test_volume_ubeswap_1_celo():
    ubeswap = Dex(protocol="Ubeswap", chain="Celo", version=1)
    hourly = ubeswap.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "Ubeswap")
    assert(hourly[0]['chain'] == "Celo")
    assert(hourly[0]['version'] == 1)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(float(hourly[0]['hourlyVolumeUSD']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)


def test_volume_pangolin_1_avalanche():
    pangolin = Dex(protocol="Pangolin", chain="avalanche", version=1)
    hourly = pangolin.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "Pangolin")
    assert(hourly[0]['chain'] == "avalanche")
    assert(hourly[0]['version'] == 1)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(float(hourly[0]['hourlyVolumeUSD']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)



def test_volume_dodoex_1_ethereum():
    dodoex = Dex(protocol="dodoex", chain="ethereum", version=2)
    hourly = dodoex.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "dodoex")
    assert(hourly[0]['chain'] == "ethereum")
    assert(hourly[0]['version'] == 2)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(hourly[0]['hourlyVolumeUSD'] == 'NA')
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)




def test_volume_dodoex_1_bsc():
    dodoex = Dex(protocol="dodoex", chain="bsc", version=2)
    hourly = dodoex.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "dodoex")
    assert(hourly[0]['chain'] == "bsc")
    assert(hourly[0]['version'] == 2)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(hourly[0]['hourlyVolumeUSD'] == 'NA')
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)


def test_volume_dodoex_1_polygon():
    dodoex = Dex(protocol="dodoex", chain="polygon", version=2)
    hourly = dodoex.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "dodoex")
    assert(hourly[0]['chain'] == "polygon")
    assert(hourly[0]['version'] == 2)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(hourly[0]['hourlyVolumeUSD'] == 'NA')
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)



def test_volume_dodoex_1_arbitrum():
    dodoex = Dex(protocol="dodoex", chain="arbitrum", version=2)
    hourly = dodoex.get_data_from_date_range(
        from_date='01/03/2022 00:00:00',
        to_date='01/03/2022 01:00:00',
        entity='pool_volume_hourly'
    )

    assert(hourly[0]['id'] != "")
    assert(hourly[0]['protocol'] == "dodoex")
    assert(hourly[0]['chain'] == "arbitrum")
    assert(hourly[0]['version'] == 2)
    assert(hourly[0]['token0'] !="")
    assert(hourly[0]['token1'] !="")
    assert(float(hourly[0]['liquidity']) >= 0)
    assert(hourly[0]['hourlyVolumeUSD'] == 'NA')
    assert(float(hourly[0]['hourlyVolumeToken0']) >= 0)
    assert(float(hourly[0]['hourlyVolumeToken1']) >= 0)
    assert(float(hourly[0]['hourlyTxns']) >= 0)
    assert(float(hourly[0]['hourStartUnix']) >= 0)