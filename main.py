import tkinter as tk
from model import PokemonModel
from view import PokemonView
from controller import PokemonController
import view

def main():
    root = tk.Tk()
    root.title("Pokedex")
    root.geometry("912x720")
    model = PokemonModel()
    view = PokemonView(root)
    controller = PokemonController(model, view)

    root.mainloop()

if __name__ == "__main__":
    main()
