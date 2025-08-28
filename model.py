import requests
import json 
import wget
import os

class PokemonModel:
    def __init__(self):
        """
        Creates/Pulls the initial data used by the Pokedex such as the Pokemon number and subsequent name of the Pokemon with that number.
        
        Args:
            self: The current instance
        """
        self.number = 1
        pokeresponse = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.number}")
        pokedata = pokeresponse.json()
        self.name = (pokedata['name'])

    def increment(self):
        """
        Handles what happens when the increase button is pressed and puts the 1 to 151 limit onto the pokedex.

        Args:
            self: The current instance
        """
        if self.number < 151:
            self.number += 1
        else:
            self.number = 1

    def decrement(self):
        """
        Handles what happens when the decreased button is pressed and puts the 1 to 151 limit onto the pokedex.

        Args:
            self: The current instance
        """
        if self.number > 1:
            self.number -= 1
        else:
            self.number = 151

    def get_value(self):
        """
        Handles all the get value requests for data updates for each new pokemon such as the name, sprite, as well as the species description
        
        Args:
            self: The current instance

        Returns:
            self.number: The ID of the pokemon displayed.
            self.name: The name of the pokemon displayed.
            self.imagename: The image of the pokemon to display.
            self.description: The brief description of the pokemon displayed.
        """
        pokeresponse = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.number}")
        pokedata = pokeresponse.json()
        self.name = pokedata['name']
        self.imageurl = pokedata['sprites']['front_default']

        species_response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.number}")
        species_data = species_response.json()

        for entry in species_data["flavor_text_entries"]:
            if entry["language"]["name"] == "en":
                description = entry["flavor_text"].replace("\n", " ").replace("\f", " ")
                break

        if os.path.exists(f"pokeimage/{self.number}.png"):
            pass
        else:
            wget.download(self.imageurl, f"{self.number}.png")
        self.imagename = (f"pokeimage/{self.number}.png")
        self.description = description
        return self.number, self.name, self.imagename, self.description
