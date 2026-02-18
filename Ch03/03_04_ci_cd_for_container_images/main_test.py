import unittest
import json
import os
from pathlib import Path
from fastapi.testclient import TestClient
from main import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        # Get the directory where this test file is located
        test_dir = Path(__file__).parent
        data_file = test_dir / "data.json"
        with open(data_file, "r") as f:
            self.data = json.load(f)

    def test_read_data(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.data)

    def test_read_data_by_guid(self):
        guid = self.data[0]["guid"]
        response = self.client.get(f"/{guid}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.data[0])

    def test_read_data_by_invalid_guid(self):
        response = self.client.get("/invalid-guid")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
