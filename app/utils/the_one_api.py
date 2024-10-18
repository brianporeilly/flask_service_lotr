import requests
import re

from app import settings

class TheOneApiClient(requests.Session):
    def __init__(self):
        super().__init__()
        self.base_url = settings.THE_ONE_API_URL
        self.headers = {
            "Authorization": f"Bearer {settings.THE_ONE_API_KEY}",
        }

    def get_characters(self):
        response = self.get(f"{self.base_url}/character")
        response.raise_for_status()
        return response.json().get("docs", [])

    def get_quotes_from_character(self, character_id: str):
        response = self.get(f"{self.base_url}/character/{character_id}/quote")
        response.raise_for_status()
        return response.json()

    def find_character_by_name(self, name: str):
        response = self.get(f"{self.base_url}/character?name=/{name}/i")
        response.raise_for_status()
        characters = response.json().get("docs", [])
        if len(characters) == 0:
            return None, None
        return characters[0]["_id"], characters[0]["name"]
