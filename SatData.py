# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/7/2024
# Description:

import json

class SatData:
    """Handles reading SAT data from a JSON file and exporting selected records to a CSV file."""

    def __init__(self, filepath='sat.json'):
        """Initializes the SatData class by loading SAT data from a specified JSON file."""
        self._data = self._load_data(filepath)

    def _load_data(self, filepath):
        """Loads SAT data from a JSON file."""
        with open(filepath, 'r') as file:
            data = json.load(file)
        # Ensure that data is a list for correct processing later
        if not isinstance(data, list):
            raise ValueError("JSON data must be a list of dictionaries")
        return data

    def save_as_csv(self, dbns):
        """Saves SAT data for specified DBNs to a CSV file named 'output.csv'."""
        headers = ["DBN", "SCHOOL NAME", "NUM OF SAT TEST TAKERS", "SAT CRITICAL READING AVG. SCORE", "SAT MATH AVG. SCORE", "SAT WRITING AVG. SCORE"]
        rows = [",".join(headers)]

        # Ensure dbns are processed correctly, even if JSON data isn't structured as expected
        for dbn in sorted(dbns):
            for school in self._data:
                if isinstance(school, dict) and school.get('dbn') == dbn:
                    # Collect data safely, accounting for commas in school names
                    school_data = [
                        school.get('dbn', ''),
                        f'"{school.get("school_name", "")}"' if ',' in school.get("school_name", "") else school.get("school_name", ""),
                        school.get('num_of_sat_test_takers', ''),
                        school.get('sat_critical_reading_avg_score', ''),
                        school.get('sat_math_avg_score', ''),
                        school.get('sat_writing_avg_score', '')
                    ]
                    rows.append(",".join(school_data))

        # Write to CSV, handling special characters and structure safely
        with open('output.csv', 'w') as csvfile:
            for row in rows:
                csvfile.write(row + '\n')






