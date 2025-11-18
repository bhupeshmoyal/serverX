import os
import json

class MockRepository:

    def __init__(self, directory="mock_data"):
        self.directory = directory
        self.cache = self._load_all()

    def _load_all(self):
        data = []
        for file in os.listdir(self.directory):
            if file.endswith(".json"):
                with open(os.path.join(self.directory, file)) as f:
                    data.append(json.load(f))
        return data

    def list_mocks(self):
        return self.cache
