import tkinter as tk
from PIL import ImageTk, Image

class PokemonView(tk.Frame):
    def __init__(self, master):
        """
        The initial screen setup of the program.
        Sets up the background of the Pokedex
        Creates the image of the initial Pokemon displayed, Bulbasaur
        Creates the number ID of the initial Pokemon displayed, Bulbasaur
        Creates the name of the initial Pokemon displayed, Bulbasaur
        Creates the description of the initialP okemon displayed, Bulbasaur
        Creates the forward button that loads the next Pokemon
        Creates the backward button that loads the previous Pokemon
        
        Args:
            self: the current instance
            master: the parent view of the whole program
        """
        super().__init__(master)

        self.image_label = tk.Label(master=master, width=1280, height=720)
        self.image_label_png = tk.PhotoImage(file = 'blankpokedex1.png')
        self.image_label['image'] = self.image_label_png
        self.image_label.place(x=0,y=0)

        self.pokeimage = tk.Label(master=master, width=384, height=384)
        img = Image.open("pokeimage/1.png")
        img = img.resize((384, 384), Image.Resampling.LANCZOS)
        self.pokeimage_png = ImageTk.PhotoImage(img)
        self.pokeimage['image'] = self.pokeimage_png
        self.pokeimage.place(x=30,y=120)
        
        self.label = tk.Label(text="1", font=("Press Start 2P", 36), master=master)
        self.label.place(x=700,y=45)
        
        self.pokename = tk.Label(text="bulbasaur", font=("Press Start 2P", 36))
        self.pokename.place(x=150, y=45)

        
        self.pokedescription = tk.Label(master, text="A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON.", font = ("Press Start 2P", 22), wraplength=475, justify="left")
        self.pokedescription.place(x=400, y=200)

        self.next_button = tk.Button(master=master, text="----------->")
        self.next_button.place(x=620, y=643)

        self.prev_button = tk.Button(master=master, text="<-----------")
        self.prev_button.place(x=530, y=643)


    def set_label(self, text):
        """
        Updates the number label, which is the ID of the pokemon displayed.

        Args:
            self: the current instance
            text: the Pokemon ID text
        """
        self.label.config(text=str(text))

    def set_pokename(self, text):
        """
        Updates the name label, which is the name of the pokemon displayed.

        Args:
            self: the current instance
            text: the Pokemon Name text
        """
        self.pokename.config(text=str(text))

    def set_pokedescription(self,text):
        """
        Updates the description label, which is the description of the pokemon displayed.

        Args:
            self: the current instance
            text: the Pokemon Description text
        """
        self.pokedescription.config(text=str(text))

    def set_pokeimage(self, pokeimage_path):
        """
        Updates the image label, which is the sprite image of the pokemon displayed.

        Args:
            self: the current instance
            pokeimage_path: the file name/path of the sprite image of the pokemon displayed.
        """
        img = Image.open(pokeimage_path)
        img = img.resize((384, 384), Image.Resampling.LANCZOS)
        self.pokeimage_png = ImageTk.PhotoImage(img)
        self.pokeimage['image'] = self.pokeimage_png
        self.pokeimage.place(x=30, y=120)
        
    def set_next_callback(self, callback):
        """
        Defines what to do for when the increment button is pressed.

        Args:
            self: the current instance
            callback: the method to run to update the data to display
        """
        self.next_button.config(command=callback)

    def set_prev_callback(self, callback):
        """
        Defines what to do for when the decrement button is pressed.

        Args:
            self: the current instance
            callback: the method to run to update the data to display
        """
        self.prev_button.config(command=callback)
