from scripts.helpful_scritps import get_account
from brownie import interface, config, network
from web3 import Web3


def main():
    get_weth()


def get_weth():
    """
    Mints WETH bt depositing ETH.
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    wei = Web3.toWei(0.000001, "ether")
    tx = weth.deposit({"from": account, "value": wei})
    tx.wait(1)
    print("Received 0.000001 WETH")
    return tx
