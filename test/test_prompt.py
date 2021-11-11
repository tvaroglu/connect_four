import unittest
from lib.prompt import Prompt

class TestPrompt(unittest.TestCase):
    def setUp(self):
        self.prompt = Prompt('world')

    def test_say_hello(self):
        self.assertEqual(self.prompt.say_hello(), 'Hello world')

if __name__ == '__main__':
    unittest.main()
