# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description:

# SatData.py
import json


class SatData:
    """Class to handle reading SAT data from a JSON file and exporting selected records to a CSV file."""

    def __init__(self, filepath='sat.json'):
        """
        Initializes the SatData class by loading SAT data from a specified JSON file.

        Args:
            filepath (str): Path to the JSON file containing SAT data.
        """
        self._data = self._load_data(filepath)

    def _load_data(self, filepath):
        """Loads SAT data from a JSON file.

        Args:
            filepath (str): Path to the JSON file.

        Returns:
            List[Dict[str, Any]]: The SAT data loaded from the file.
        """
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data

    def save_as_csv(self, dbns):
        """Saves SAT data for specified DBNs to a CSV file named 'output.csv'.

        Args:
            dbns (List[str]): The DBNs to include in the output CSV file.
        """
        headers = ["DBN", "SCHOOL NAME", "NUM OF SAT TEST TAKERS", "SAT CRITICAL READING AVG. SCORE",
                   "SAT MATH AVG. SCORE", "SAT WRITING AVG. SCORE"]
        rows = [headers]

        for dbn in sorted(dbns):
            for school in self._data:
                if school['dbn'] == dbn:
                    row = [school['dbn'],
                           '"' + school['school_name'] + '"' if ',' in school['school_name'] else school['school_name'],
                           school['num_of_sat_test_takers'], school['sat_critical_reading_avg_score'],
                           school['sat_math_avg_score'], school['sat_writing_avg_score']]
                    rows.append(row)

        with open('output.csv', 'w') as csvfile:
            for row in rows:
                csvfile.write(','.join(row) + '\n')




