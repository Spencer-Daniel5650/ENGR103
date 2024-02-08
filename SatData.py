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

            # Write rows corresponding to DBNs in the list
            for row in self.data:
                # Ensure each row is a dictionary
                if not isinstance(row, dict):
                    continue  # Skip non-dictionary items

                if row.get('DBN') in DBNS:
                    # Format row values as CSV string
                    csv_row = '{},{},{},{},{},{}\n'.format(
                        row['DBN'],
                        '"' + row['SCHOOL NAME'] + '"',  # Enclose name in double quotes
                        row['Num of SAT Test Takers'],
                        row['SAT Critical Reading Avg. Score'],
                        row['SAT Math Avg. Score'],
                        row['SAT Writing Avg. Score']
                    )
                    file.write(csv_row)


sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)
