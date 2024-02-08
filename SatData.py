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
        """Loads SAT data from a JSON file, accommodating different possible structures."""
        with open(filepath, 'r') as file:
            raw_data = json.load(file)
        # Adjust for the JSON structure; assuming top-level key might hold the data list
        if isinstance(raw_data, dict):
            # Assuming there's a known key that holds the list of data; adjust 'key_name' as necessary
            for key in raw_data:
                if isinstance(raw_data[key], list):
                    return raw_data[key]
            raise ValueError("JSON does not contain a list under any top-level key")
        elif isinstance(raw_data, list):
            return raw_data
        else:
            raise ValueError("JSON structure is not recognized")
        return []

    def save_as_csv(self, dbns):
        """Saves SAT data for specified DBNs to a CSV file named 'output.csv'."""
        headers = ["DBN", "SCHOOL NAME", "NUM OF SAT TEST TAKERS", "SAT CRITICAL READING AVG. SCORE", "SAT MATH AVG. SCORE", "SAT WRITING AVG. SCORE"]
        rows = [",".join(headers)]

        for dbn in sorted(dbns):
            for school in self._data:
                if school.get('dbn') == dbn:
                    school_data = [
                        school.get('dbn', ''),
                        f'"{school.get("school_name", "")}"' if ',' in school.get("school_name", "") else school.get("school_name", ""),
                        school.get('num_of_sat_test_takers', ''),
                        school.get('sat_critical_reading_avg_score', ''),
                        school.get('sat_math_avg_score', ''),
                        school.get('sat_writing_avg_score', '')
                    ]
                    rows.append(",".join(school_data))

        with open('output.csv', 'w') as csvfile:
            for row in rows:
                csvfile.write(row + '\n')






