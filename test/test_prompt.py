import unittest
from lib.prompt import Prompt

class TestPrompt(unittest.TestCase):
    def setUp(self):
        self.prompt = Prompt()

    def test_welcome(self):
        self.assertEqual(self.prompt.welcome(), 'Welcome to ConnectFour!')

    def test_request_name(self):
        self.assertEqual(self.prompt.request_name(), "What is your name?\n > ")


if __name__ == '__main__':
    unittest.main()
