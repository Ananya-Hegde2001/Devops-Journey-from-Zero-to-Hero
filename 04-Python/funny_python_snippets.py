
# Funny Python snippets to make coding more enjoyable

# Print a random joke
import requests
response = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = response.json()
print(f"{joke['setup']} - {joke['punchline']}")

# Generate a random excuse
excuses = [
    "My dog ate my code.",
    "I thought I was working on the main branch.",
    "It worked on my machine.",
    "I was abducted by aliens."
]
import random
print(random.choice(excuses))

# Create a function that always returns "42"
def ultimate_answer():
    return 42

print(f"The ultimate answer to life, the universe, and everything is {ultimate_answer()}")