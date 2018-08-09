# The program should ask the user to enter 2+ paramater
# one being a path to the local copy of the site
# the other being one or more URLs

class UserCLI:
    def analyzewebsite(*args):
        if len(args) < 2:
            raise TypeError("There must be at least 2 arguments")
        for argument in args:
            pass

