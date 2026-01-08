import requests

class CoreBankingClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def get_headers(self) -> dict:
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def sync_user_data(self, user_data: dict) -> dict:
        response = requests.post(f'{self.base_url}/users/sync', json=user_data, headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def sync_account_data(self, account_data: dict) -> dict:
        response = requests.post(f'{self.base_url}/accounts/sync', json=account_data, headers=self.get_headers())
        response.raise_for_status()
        return response.json()