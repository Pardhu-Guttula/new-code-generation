from typing import Dict
from backend.integrations.core_banking.client import CoreBankingClient
import logging

class CoreBankingSyncService:
    def __init__(self, client: CoreBankingClient):
        self.client = client
        self.logger = logging.getLogger(__name__)

    def sync_user_data(self, user_data: Dict) -> Dict:
        try:
            return self.client.sync_user_data(user_data)
        except Exception as e:
            self.logger.error(f'Failed to sync user data: {e}')
            raise

    def sync_account_data(self, account_data: Dict) -> Dict:
        try:
            return self.client.sync_account_data(account_data)
        except Exception as e:
            self.logger.error(f'Failed to sync account data: {e}')
            raise