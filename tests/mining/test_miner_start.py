import random

import gevent


def test_miner_start(web3_empty, wait_for_miner_start):
    web3 = web3_empty

    # sanity
    assert web3.eth.mining
    assert web3.miner.hashrate

    web3.miner.stop()

    with gevent.Timeout(60):
        while web3.eth.mining or web3.eth.hashrate:
            gevent.sleep(random.random())

    assert not web3.eth.mining
    assert not web3.miner.hashrate

    web3.miner.start(1)

    wait_for_miner_start(web3)

    assert web3.eth.mining
    assert web3.miner.hashrate
