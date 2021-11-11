import unittest
from lib.hello import Hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        h = Hello('world')
        self.assertEqual(h.say_hello(), 'hello world')

if __name__ == '__main__':
    unittest.main()
