# Motivation generator

import requests
import random

def get_motivational_quote():
    response = requests.get("https://type.fit/api/quotes")
    quotes = response.json()
    quote = random.choice(quotes)
    return f"{quote['text']} - {quote['author']}"

print(get_motivational_quote())