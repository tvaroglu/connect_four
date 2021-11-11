import unittest
from lib.hello import Hello

class TestHello(unittest.TestCase):
    def setUp(self):
        self.h = Hello('world')

    def test_say_hello(self):
        self.assertEqual(self.h.say_hello(), 'hello world')

if __name__ == '__main__':
    unittest.main()
