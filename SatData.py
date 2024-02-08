# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description:

import json
import csv


class SatData:
    def __init__(self, filename='sat.json'):
        self.__data = []  # Private data member to store SAT data
        try:
            with open(filename, 'r') as file:
                # Load the JSON data; assuming the top-level structure is a list
                data_loaded = json.load(file)
                # If the data is nested, adjust accordingly here
                self.__data = data_loaded if isinstance(data_loaded, list) else []
        except FileNotFoundError:
            print(f'File {filename} not found.')

    def save_as_csv(self, dbns):
        # Filter data for the provided DBNs
        filtered_data = [entry for entry in self.__data if entry['dbn'] in dbns]

        # Sort the filtered data by DBN
        sorted_data = sorted(filtered_data, key=lambda x: x['dbn'])

        # Write to CSV
        with open('output.csv', 'w', newline='') as file:
            if sorted_data:
                csv_writer = csv.writer(file)
                # Extract headers from the first item, assuming all items have the same structure
                headers = list(sorted_data[0].keys())
                csv_writer.writerow(headers)

                for entry in sorted_data:
                    row = [entry.get(header, '') for header in headers]
                    csv_writer.writerow(row)
            else:
                print("No matching DBNs found in the data.")

