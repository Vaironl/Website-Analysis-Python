import unittest

import Analysis
from Analysis.usercli import setupArguments, startAnalysis

emptylist = []

for i in range (0,2000):
    emptylist.append(i)

class TestUserCLI(unittest.TestCase):

    def test_setupArguments(self):
        setupArguments(emptylist)

    def test_startAnalysis(self):
        startAnalysis()