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
        if len(argv) == 3:
            urls = argv[2]
            if urls == []:
                return False
            if len(urls) < 0 or len(urls) > 1000:
                return False
            return True
        return False

    def print_results(self):
        """Results to be printed"""
        pass

    def get_arv(self):
        return argv
