# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description:

import json
import csv


class SatData:
    def __init__(self, filename='sat.json'):
        # Private data member to store SAT data
        self.__data = []
        try:
            with open(filename, 'r') as file:
                # Assuming the JSON structure directly contains the relevant data array
                self.__data = json.load(file)
        except FileNotFoundError:
            print(f'File {filename} not found.')

    def save_as_csv(self, dbns):
        # Headers as specified in the error message
        headers = ['DBN', 'School Name', 'Number of Test Takers', 'Critical Reading Mean', 'Mathematics Mean',
                   'Writing Mean']

        # Filter data for the provided DBNs
        filtered_data = [entry for entry in self.__data if entry['DBN'] in dbns]

        # Sort the filtered data by DBN
        sorted_data = sorted(filtered_data, key=lambda x: x['DBN'])

        # Write to CSV, ensuring we use the specified headers
        with open('output.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers)  # Write the headers to the CSV file

            for entry in sorted_data:
                # Create a row for each entry, ordered according to the headers
                row = [entry.get(header, '') for header in headers]
                csv_writer.writerow(row)

        if not sorted_data:
            print("No matching DBNs found in the data.")

