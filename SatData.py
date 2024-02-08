# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description:

import json

class SatData:
    def __init__(self):
        with open('sat.json', 'r') as file:
            self.data = json.load(file)

    def save_as_csv(self, DBNS):  # Use DBNS parameter instead of dbns
        # Sort DBNs in ascending order
        DBNS.sort()  # Correct case for the parameter

        # Open output file for writing
        with open('output.csv', 'w') as file:
            # Write column headers
            file.write('DBN,SCHOOL NAME,Num of SAT Test Takers,SAT Critical Reading Avg. Score,SAT Math Avg. Score,SAT Writing Avg. Score\n')

            # Write rows corresponding to DBNs in the list
            for row in self.data:
                if row['DBN'] in DBNS:  # Use DBNS parameter instead of dbns
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