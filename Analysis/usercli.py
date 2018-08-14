# The program should ask the user to enter 2+ paramater
# one being a path to the local copy of the site
# the other being one or more URLs

import sys

arguments = None

if __name__ != "__main__":
    def setupArguments(args):
        global arguments
        arguments = args

elif __name__ == "__main__":
    global arguments
    arguments = sys.argv


def startAnalysis():
    if len(arguments) < 2:
        raise TypeError("There must be at least 2 arguments")
    elif len(arguments) > 1001:
        raise TypeError("There must be no more than 1,001 arguments")
