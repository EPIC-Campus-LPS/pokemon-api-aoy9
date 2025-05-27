class PokemonModel:
    def __init__(self):
        self.number = 0

    def increment(self):
        self.number += 1

    def decrement(self):
        self.number -= 1

    def get_value(self):
        return self.number
