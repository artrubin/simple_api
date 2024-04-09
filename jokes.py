import requests
from random import choice
import pyfiglet
from termcolor import colored


header = pyfiglet.figlet_format("DAD'S JOKES")
header = colored(header, color="yellow")
print(header)
search_term = input("Please enter the search term for a joke >> ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(url, headers={"Accept": "application/json"}, params={"term": search_term}).json()
results = response["results"]
num_jokes = len(results)
if num_jokes > 1:
    print(f"I've got {num_jokes} jokes about the {search_term}. Here is one: ")
    print(choice(results)['joke'])
elif num_jokes == 1:
    print(f"I've got {num_jokes} joke about the {search_term}. Here it is: ")
    print((results)[0]['joke'])
else:
    print(f"I've got no jokes about the {search_term}. Please try again ")







