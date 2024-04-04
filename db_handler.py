import json
import os

class JSONDatabase:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        if not os.path.exists(self.filename):
            # File doesn't exist
            return None
        with open(self.filename, "r") as file:
            data = json.load(file)
        return data

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)