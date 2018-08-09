import unittest

from Analysis.usercli import UserCLI


class UserCLITests(unittest.TestCase):
    def test_analyzewebsite(self):
        with self.assertRaises(TypeError):
            UserCLI.analyzewebsite()

