import unittest
import json
from index import handler

class TestHandler(unittest.TestCase):
    def setUp(self):
        # Load the data.json file into a list of dictionaries
        with open("data.json", "r") as f:
            self.data = json.load(f)

    def test_root_path(self):
        # Create a valid event for the root path "/"
        event = {
            "rawPath": "/"
        }

        # Call the handler function with the event
        response = handler(event, None)

        # Validate the response
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["headers"]["Content-Type"], "text/json")
        self.assertEqual(json.loads(response["body"]), self.data)

    def test_valid_paths(self):
        # Test for paths with values from 1 to 12
        for i in range(1, 13):
            event = {
                "rawPath": f"/{i}"
            }

            # Call the handler function with the event
            response = handler(event, None)

            # Find the corresponding item in the data list
            item = next((x for x in self.data if x["id"] == str(i)), None)

            if item:
                # If the item is found, validate the response
                self.assertEqual(response["statusCode"], 200)
                self.assertEqual(response["headers"]["Content-Type"], "text/json")
                self.assertEqual(json.loads(response["body"]), item)
            else:
                # If the item is not found, validate the 404 response
                self.assertEqual(response["statusCode"], 404)
                self.assertEqual(response["headers"]["Content-Type"], "text/json")
                self.assertEqual(json.loads(response["body"]), {
                    "message": f"id {i} not found",
                    "event": event,
                    "id": str(i)
                })

if __name__ == "__main__":
    unittest.main()

