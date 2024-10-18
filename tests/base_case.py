from app import app
import unittest
import os


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        os.environ["APP_SETTINGS"] = "config.TestingConfig"
        self.app = app
        self.client = self.app.test_client()
        self.headers = None
