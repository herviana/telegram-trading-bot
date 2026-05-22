"""Wallet management"""

from eth_account import Account
from typing import Dict, Optional
from bot.logger import logger
from bot.utils.encryption import EncryptionManager


class WalletManager:
    """Manage wallets and private keys"""

    def __init__(self, encryption_key: str = None):
        """Initialize wallet manager"""
        self.encryption = EncryptionManager(encryption_key)

    def create_wallet(self) -> Dict[str, str]:
        """Create new wallet"""
        try:
            account = Account.create()
            
            return {
                "address": account.address,
                "private_key": account.key.hex(),
            }
        
        except Exception as e:
            logger.error(f"Error creating wallet: {str(e)}")
            raise

    def import_wallet(self, private_key: str) -> Dict[str, str]:
        """Import wallet from private key"""
        try:
            account = Account.from_key(private_key)
            
            return {
                "address": account.address,
                "private_key": account.key.hex(),
            }
        
        except Exception as e:
            logger.error(f"Error importing wallet: {str(e)}")
            raise

    def encrypt_private_key(self, private_key: str) -> str:
        """Encrypt private key"""
        return self.encryption.encrypt(private_key)

    def decrypt_private_key(self, encrypted_key: str) -> str:
        """Decrypt private key"""
        return self.encryption.decrypt(encrypted_key)

    def is_valid_private_key(self, private_key: str) -> bool:
        """Validate private key format"""
        try:
            Account.from_key(private_key)
            return True
        except Exception:
            return False

    def is_valid_address(self, address: str) -> bool:
        """Validate Ethereum address"""
        try:
            from eth_utils import is_address
            return is_address(address)
        except Exception:
            return False
