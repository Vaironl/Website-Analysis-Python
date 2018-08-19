# has mutliple pages

from Analysis import webpage

web_pages = []
urls = []
mapped_urls = []
local_path = ""

def validate_local_path(self):
    # does the local path exist?
    # is the local path readable? (No weird permission errors)
    pass


def validate_urls(self):
    # Is this URL malformed?
    # Is there a HTTP error?
    pass


def map_urls(self):
    # strip the site root and check it is valid
    # internal should be analized
    # external should not
    pass
