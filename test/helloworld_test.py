import unittest

def greetings(name):
    return "Hello, " + name + "!"

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(greetings("Vairon"), "Hello, Vairon!")
