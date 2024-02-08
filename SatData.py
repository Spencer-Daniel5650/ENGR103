# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description:

import json
class SatData:
    def __init__(self, filename='sat.json'):
        # Private data member to store SAT data
        self.__data = []
        try:
            with open(filename, 'r') as file:
                self.__data = json.load(file)
        except FileNotFoundError:
            print(f'File {filename} not found.')

    def save_as_csv(self, dbns):
        # Filter data for the provided DBNs
        filtered_data = [entry for entry in self.__data if entry['dbn'] in dbns]

        # Sort the filtered data by DBN
        sorted_data = sorted(filtered_data, key=lambda x: x['dbn'])

        # Write to CSV
        with open('output.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            # Assuming you know the headers or extract from the first item if list is not empty
            headers = ['dbn', 'school_name', 'num_of_sat_test_takers', 'sat_critical_reading_avg_score',
                       'sat_math_avg_score', 'sat_writing_avg_score'] if sorted_data else []
            csv_writer.writerow(headers)

            for entry in sorted_data:
                row = [entry.get(header, '') for header in headers]
                csv_writer.writerow(row)

# Example usage
# sat_data = SatData()
# sat_data.save_as_csv(['01M292', '02M294'])  # Example DBNs
