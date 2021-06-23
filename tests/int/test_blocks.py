from deficrawler.block import Block


def test_block_bsc():
    block = Block(protocol='block', chain='bsc', version='1')
    block_info = block.get_block_at_timestamp(timestamp=1623673813)
    assert(int(block_info[0]['number']) == 8289859)

    block_info = block.get_block_info(block_number=8289859)
    assert(int(block_info[0]['timestamp']) == 1623673811)



def test_block_ethereum():
    block = Block(protocol='block', chain='Ethereum', version='1')
    block_info = block.get_block_at_timestamp(timestamp=1623673813)
    assert(int(block_info[0]['number']) == 12632560)

    block_info = block.get_block_info(block_number=12632560)
    assert(int(block_info[0]['timestamp']) == 1623673813)


def test_block_polygon():
    block = Block(protocol='block', chain='Polygon', version='1')
    block_info = block.get_block_at_timestamp(timestamp=1617176896)
    print(block_info[0]['number'])
    assert(int(block_info[0]['number']) == 12685220)

    block_info = block.get_block_info(block_number=12685220)
    assert(int(block_info[0]['timestamp']) == 1617176896)



