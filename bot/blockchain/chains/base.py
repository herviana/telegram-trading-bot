"""Base chain configuration"""

from bot.blockchain.web3_client import Web3Client


class BaseChain:
    """Base (formerly Base Mainnet) chain support"""

    RPC_URL = "https://mainnet.base.org"
    CHAIN_ID = 8453
    CHAIN_NAME = "base"
    CURRENCY = "ETH"
    BLOCK_EXPLORER = "https://basescan.org"

    def __init__(self):
        """Initialize Base chain client"""
        self.client = Web3Client(
            provider_url=self.RPC_URL,
            chain_id=self.CHAIN_ID
        )

    def get_balance(self, address: str) -> float:
        """Get balance on Base"""
        return self.client.get_balance(address)

    def get_gas_price(self) -> dict:
        """Get gas price on Base"""
        return self.client.get_gas_price()
