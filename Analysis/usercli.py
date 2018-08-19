from sys import argv


class UserCLI:
    arguments = None
    valid_arguments = False

    def setup_test(self, in_argv):
        """Helps to test class"""
        global argv
        argv = in_argv

        pass

    def start_analysis(self):
        return False

    def print_results(self):
        #
        pass

    def get_arv(self):
        return argv
