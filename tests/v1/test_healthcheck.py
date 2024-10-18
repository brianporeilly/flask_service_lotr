from tests.base_case import BaseTestCase
import json


class TestHealthcheck(BaseTestCase):
    def test_get_healthcheck(self):
        response = self.client.get(f"/v1/healthcheck/", headers=self.headers)
        self.assertEqual(response.status_code, 200, response.data)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["message"], "I'm healthy!")
