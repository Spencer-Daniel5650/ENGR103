# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description:Nobel Prize data from a JSON file,
# providing functionality to search and return a sorted list of laureates' surnames for specified year and category.

import json

class NobelData:
    def __init__(self, filepath='nobels.json'):
        """
        Initializes the NobelData class by reading Nobel Prize data from a JSON file.

        Parameters:
        - filepath (str): The path to the JSON file containing Nobel Prize data.
        """
        self._data = self._load_data(filepath)

    def _load_data(self, filepath):
        """
        Loads Nobel Prize data from the specified JSON file.

        Parameters:
        - filepath (str): The path to the JSON file.

        Returns:
        - data (dict): The loaded Nobel Prize data.
        """
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data

    def search_nobel(self, year, category):
        """
        Searches for Nobel Prize winners based on the specified year and category.

        Parameters:
        - year (str): The year of the Nobel Prize.
        - category (str): The category of the Nobel Prize.

        Returns:
        - winners (list of str): A sorted list of surnames of the winners.
        """
        winners = []
        for prize in self._data['prizes']:
            if prize['year'] == year and prize['category'] == category:
                for laureate in prize['laureates']:
                    winners.append(laureate['surname'])
        return sorted(winners)

