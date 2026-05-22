"""Web3 client for blockchain interactions"""

from web3 import Web3
from eth_account import Account
from typing import Optional, Dict, Any
from bot.config import get_settings
from bot.logger import logger

config = get_settings()


class Web3Client:
    """Web3 client wrapper"""

    def __init__(self, provider_url: str = None, chain_id: int = None):
        """Initialize Web3 client"""
        self.provider_url = provider_url or config.web3_provider_url
        self.chain_id = chain_id or config.web3_chain_id
        self.w3 = Web3(Web3.HTTPProvider(self.provider_url))
        
        if not self.w3.is_connected():
            logger.error(f"Failed to connect to {self.provider_url}")
            raise ConnectionError(f"Cannot connect to {self.provider_url}")

    def get_balance(self, address: str) -> float:
        """Get ETH balance for address"""
        try:
            balance_wei = self.w3.eth.get_balance(address)
            return self.w3.from_wei(balance_wei, 'ether')
        except Exception as e:
            logger.error(f"Error getting balance: {str(e)}")
            raise

    def get_gas_price(self) -> Dict[str, float]:
        """Get current gas prices"""
        try:
            gas_price_wei = self.w3.eth.gas_price
            gas_price_gwei = self.w3.from_wei(gas_price_wei, 'gwei')
            
            return {
                "standard": gas_price_gwei,
                "fast": gas_price_gwei * 1.2,
                "instant": gas_price_gwei * 1.5,
            }
        except Exception as e:
            logger.error(f"Error getting gas price: {str(e)}")
            raise

    def get_nonce(self, address: str) -> int:
        """Get nonce for address"""
        try:
            return self.w3.eth.get_transaction_count(address)
        except Exception as e:
            logger.error(f"Error getting nonce: {str(e)}")
            raise
