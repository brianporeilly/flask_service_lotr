import json
import random

from app.utils.errors import AppError
from app.utils.the_one_api import TheOneApiClient

# routes from the-one-api:
# /character
# /character/{id}/quote


def lotr_quote(name: str) -> (str, int):
    client = TheOneApiClient()

    character_id, character_name = client.find_character_by_name(name)
    if character_id is None:
        return json.dumps({"message": "Character not found"}), 404

    response = client.get_quotes_from_character(character_id)
    quotes = response.get("docs", [])

    quote = get_random_quote_from_quotes(quotes)
    if quote is None:
        return json.dumps({"message": "No quotes found"}), 404

    response = {
        "character": character_name,
        "searched_name": name,
        "quote": quote,
    }

    return json.dumps(response), 200


def get_random_quote_from_quotes(quotes):
    count = len(quotes)
    if count == 0:
        return None
    quote_index = random.randint(0, count - 1)
    return quotes[quote_index]["dialog"]
