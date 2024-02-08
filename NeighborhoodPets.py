# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description: manages pet information with features to add, delete, and find a pet's owner, and handle pet data via JSON files

import json

# Define a custom exception for duplicate pet names
class DuplicateNameError(Exception):
    pass

class NeighborhoodPets:
    def __init__(self):
        # Initialize a private dictionary to store pet info with pet name as key
        self.__pets = {}

    def add_pet(self, name, species, owner):
        # Check if pet name already exists
        if name in self.__pets:
            raise DuplicateNameError(f"A pet with the name {name} already exists.")
        self.__pets[name] = {"species": species, "owner": owner}

    def delete_pet(self, name):
        # Remove the pet by name
        if name in self.__pets:
            del self.__pets[name]

    def get_owner(self, name):
        # Return the owner of the pet
        if name in self.__pets:
            return self.__pets[name]["owner"]
        return None

    def save_as_json(self, filename):
        # Save pet data to a JSON file
        with open(filename, 'w') as file:
            json.dump(self.__pets, file)

    def read_json(self, filename):
        # Load pet data from a JSON file
        with open(filename, 'r') as file:
            self.__pets = json.load(file)

    def get_all_species(self):
        # Return a set of all pet species
        return {pet_info["species"] for pet_info in self.__pets.values()}

