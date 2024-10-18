from tests.base_case import BaseTestCase
import json


class TestHealthcheck(BaseTestCase):
    def test_lotr_quote_valid_names(self):
        valid_names = ["frodo", "samwise", "gandalf", "legolas"]
        for name in valid_names:
            response = self.client.get(f"/v1/lotr-quote/{name}", headers=self.headers)
            self.assertEqual(response.status_code, 200, response.data)
            data = json.loads(response.data.decode("utf-8"))
            self.assertEqual(data["searched_name"], name, data)
            self.assertTrue(type(data["quote"]) == str, data["quote"])

    def test_lotr_quote_invalid_names(self):
        invalid_names = ["slartibartfast", "farnsworth"]
        for name in invalid_names:
            response = self.client.get(f"/v1/lotr-quote/{name}", headers=self.headers)
            self.assertEqual(response.status_code, 404, response.data)
            data = json.loads(response.data.decode("utf-8"))
            self.assertEqual(data["message"], "Character not found")
