
# Lab 3: Pokemon API

## Objective

- Use the PokeAPI to get information about a Pokemon given its number with the `requests` library
- Create a program that displays the image and name of a Pokemon with `tkinter`

## Sample Implementation

[Screencast from 2025-05-13 09-53-33.webm](https://github.com/user-attachments/assets/e08a0680-5b2c-42d6-b92f-379f68f48da8)


## Getting Started

1. Get familiar with how to use GET and POST requests with the `requests`library in Python. Once you can send and receive both kinds requests consistently, then move on to the next step. 
	1. [Requests Module Reference](https://www.w3schools.com/python/module_requests.asp)
	2. [Geeks for Geeks Tutorial](https://www.geeksforgeeks.org/get-post-requests-using-python/)
	3. [JSON Placeholder](https://jsonplaceholder.typicode.com/) - sample website to practice requests with
## PokeAPI and tkinter

 1. Use the [PokeAPI](https://pokeapi.co/) to get information about a Pokemon, given it's number. You will need the name and the image of the Pokemon. For the image, you will want to download it onto your computer. You can set something up to delete the images as part of the program so they don't pile up on your computer.
 2. Then create a `tkinter` application to display your image and name. Here is a quick tutorial on [tkinter](https://realpython.com/python-gui-tkinter/). For this program, separate your program into a **Model-View-Controller** architecture. 
![Pasted image 20250506111836](https://github.com/user-attachments/assets/f5de7cbf-7618-493b-884f-69c13f610080)


## docstrings

1. Once your program is complete, add [docstrings](https://www.geeksforgeeks.org/python-docstrings/) comments to your program. For each class and method, add a docstring comment to explain the method or class surrounded by triple quotes. Use Google's style of docstrings that list the arguments and return type.  
```
def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of a and b.
    """
    return a * b
print(multiply_numbers(3,5))
```


## Deliverables
- Working program with a docstring comments. 


## Rubric

- 9 pts - Contains all required components and uses professional language
- 8 pts - Contains all required components, but uses unprofessional language, formating, etc. 
- 6 pts - Contains some, but not all, of the required components
- 4 pts - Did not submit
