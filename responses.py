from random import choice, randint
import openPlaces

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '-openplace':
        return (str)(openPlaces.GetOpenRestaurants())