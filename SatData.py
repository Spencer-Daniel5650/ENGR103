# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description:

import json

class SatData:
    def __init__(self, filename):
        # Load the JSON data
        with open(filename, 'r') as file:
            self.__data = json.load(file)

    def save_as_csv(self, dbns):
        # Column headers hardcoded based on the provided description and example
        column_headers = ["DBN", "SCHOOL NAME", "NUM OF SAT TEST TAKERS", "SAT CRITICAL READING AVG. SCORE", "SAT MATH AVG. SCORE", "SAT WRITING AVG. SCORE"]
        rows = [",".join(column_headers)]  # Start with headers

        # Sort the data by DBN to ensure output is in ascending order
        sorted_data = sorted([school for school in self.__data if school["DBN"] in dbns], key=lambda x: x["DBN"])

        # Construct CSV rows
        for school in sorted_data:
            row = []
            for header in column_headers:
                # Handle commas in school names
                value = str(school[header])
                if "," in value:
                    value = f'"{value}"'  # Enclose in double quotes
                row.append(value)
            rows.append(",".join(row))

        # Write to CSV file
        with open("output.csv", 'w') as file:
            file.write("\n".join(rows))

# Example usage:
# sat_data = SatData("sat.json")
# sat_data.save_as_csv(["02M047", "21K410"])  # Example DBNs
