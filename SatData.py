# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description:

import json


class SatData:
    def __init__(self):
        with open('sat.json', 'r') as file:
            self.data = json.load(file)

    def save_as_csv(self, DBNS):
        # Ensure DBNS is a list and sort it in ascending order
        if not isinstance(DBNS, list):
            raise ValueError("DBNS must be a list")
        DBNS.sort()

        # Open output file for writing
        with open('output.csv', 'w') as file:
            # Write column headers
            file.write(
                'DBN,SCHOOL NAME,Num of SAT Test Takers,SAT Critical Reading Avg. Score,SAT Math Avg. Score,SAT Writing Avg. Score\n')

            # Keep track of found DBNs
            found_dbns = []

            # Write rows corresponding to DBNs in the list
            for row in self.data:
                # Ensure each row is a dictionary
                if not isinstance(row, dict):
                    continue  # Skip non-dictionary items

                # Check if the row's DBN is in the list and write to file if so
                if row.get('DBN') in DBNS:
                    found_dbns.append(row.get('DBN'))  # Add found DBN to the list
                    csv_row = '{},{},{},{},{},{}\n'.format(
                        row['DBN'],
                        '"' + row['SCHOOL NAME'] + '"',  # Enclose name in double quotes
                        row['Num of SAT Test Takers'],
                        row['SAT Critical Reading Avg. Score'],
                        row['SAT Math Avg. Score'],
                        row['SAT Writing Avg. Score']
                    )
                    file.write(csv_row)

            # Check if all DBNS were found
            not_found_dbns = set(DBNS) - set(found_dbns)
            if not_found_dbns:
                print(f"Warning: The following DBNs were not found in the dataset: {not_found_dbns}")


sd = SatData()
dbns = ["01M292", "01M448"]  # Example DBNs that failed in your test
sd.save_as_csv(dbns)
