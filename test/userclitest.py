import unittest

from Analysis.usercli import UserCLI


class TestUserCLI(unittest.TestCase):
    def test_setupArguments(self):

        empty_list = []
        one_arg_list = []
        two_arg_list = []
        valid_range_list = []
        over_sized_list = []

        for i in range(0, 20):
            valid_range_list.append(i)

        for i in range(0, 2000):
            over_sized_list.append(i)

        self.assertEqual(UserCLI.setupArguments(two_arg_list), "Number of arguments are valid!")
        self.assertEqual(UserCLI.setupArguments(valid_range_list), "Number of arguments are valid!")

        with self.assertRaises(TypeError):
            UserCLI.setupArguments(empty_list)

        with self.assertRaises(TypeError):
            UserCLI.setupArguments(one_arg_list)

        with self.assertRaises(TypeError):
            UserCLI.setupArguments(over_sized_list)

    def test_startAnalysis(self):
        UserCLI.startAnalysis()
        #Validate Path and validate links in startAnalysis
        #If path is not valid throw an error
        #If url(s) are not valid throw an error
