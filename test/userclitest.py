import unittest

from Analysis.usercli import UserCLI


class TestUserCLI(unittest.TestCase):
    two_arg_list = []
    valid_range_list = []
    over_sized_list = []

    for i in range(0, 1000):
        valid_range_list.append(i)

    for i in range(0, 2000):
        over_sized_list.append(i)

    def test_start_analysis_zero_arguments(self):

        cli = UserCLI()

        # no arguments passed
        argv = ['program name']
        cli.setup_test(argv)
        self.assertEqual(cli.get_arv(), argv)
        self.assertEqual(cli.get_arv(), argv)
        self.assertFalse(cli.start_analysis())

    def test_start_analysis_one_argument(self):

        cli = UserCLI()

        # one argument passed
        argv = ['program name', 'local_path']
        cli.setup_test(argv)
        self.assertEqual(cli.get_arv(), argv)
        self.assertFalse(cli.start_analysis())

    def test_start_analysis_two_invalid(self):

        cli = UserCLI()

        # two arguments passed, one invalid as an empty list
        argv = ['program name', 'local_path', []]
        cli.setup_test(argv)
        self.assertEqual(cli.get_arv(), argv)
        self.assertFalse(cli.start_analysis())

        # two arguments passed, one invalid as an over sized urls list
        argv = ['program name', 'local_path', self.over_sized_list]
        cli.setup_test(argv)
        self.assertEqual(cli.get_arv(), argv)
        self.assertFalse(cli.start_analysis())

    def test_start_analysis_two_valid(self):

        cli = UserCLI()

        # two arguments passed, both valid
        argv = ['program name', 'local_path', ['one_url']]
        cli.setup_test(argv)
        self.assertEqual(cli.get_arv(), argv)
        self.assertTrue(cli.start_analysis())

        # two arguments passed, both valid, urls are exactly within 1000 accepted limit
        argv = ['program name', 'local_path', self.valid_range_list]
        cli.setup_test(argv)
        self.assertEqual(cli.get_arv(), argv)
        self.assertTrue(cli.start_analysis())
