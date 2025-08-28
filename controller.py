class PokemonController:
    def __init__(self, model, view):
        """
        Establishes the initial variables like model and view and redirecting when the increment/decrement buttons are pressed.
        
        Args:
            self: the current instance.
            model: the initial state of model.py
            view: the initial state of view.py
        """
        self.model = model
        self.view = view
        self.view.set_next_callback(self.handle_increment)
        self.view.set_prev_callback(self.handle_decrement)

    def handle_increment(self):
        """
        directs what is happening when increment button is pressed and relays the data to the view.py functions.

        Args:
            self: the current instance
        """
        self.model.increment()
        num, name, image, description = self.model.get_value()
        self.view.set_label(num)
        self.view.set_pokename(name)
        self.view.set_pokeimage(image)
        self.view.set_pokedescription(description)

    def handle_decrement(self):
        """
        directs what is happening when the decrement button is pressed and relays the data to the view.py functions.

        Args:
            self: the current instance
        """
        self.model.decrement()
        num, name, image, description = self.model.get_value()
        self.view.set_label(num)
        self.view.set_pokename(name)
        self.view.set_pokeimage(image)
        self.view.set_pokedescription(description)
