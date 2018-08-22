import unittest

from Analysis.website import map_urls, validate_local_path, validate_urls


class TestWebsite(unittest.TestCase):

    def test_validate_local_path_valid(self):
        test_website_path = "test/testwebsite"
        self.assertTrue(validate_local_path(test_website_path))

    def test_validate_local_path_invalid(self):
        invalid_website_path = "test/somebadlocalpath"
        self.assertFalse(validate_local_path(invalid_website_path))

    def test_validate_urls(self):
        # use django to validate
        all_urls = [
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Directory/outline/index.html",
            "https://www.cs.odu.edu/~tkennedy/doesnotexist.html",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Public/syllabus/index.html",
            "https://www.arandomnonexistentwebsite.com",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum29183094/Public/syllabus/index.html",
            "google.com"
        ]

        valid_urls = [
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Directory/outline/index.html",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Public/syllabus/index.html",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum29183094/Public/syllabus/index.html"
        ]

        self.assertEqual(validate_urls(all_urls), valid_urls)

    def test_map_urls(self):
        site_root = "www.cs.odu.edu/~tkennedy/cs350/sum18/"

        all_urls = [
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Directory/outline/index.html",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Directory/policies/index.html",
            "https://online.odu.edu/how-to-succeed-as-an-online-student",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Public/syllabus/index.html",
            "https://shibboleth.odu.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s1",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Directory/library/index.html",
            "https://www.odu.edu/ts/helpdesk",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum29183094/Public/syllabus/index.html"
        ]

        valid_urls = [
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Directory/outline/index.html",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Directory/policies/index.html",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Public/syllabus/index.html",
            "https://www.cs.odu.edu/~tkennedy/cs350/sum18/Directory/library/index.html"
        ]

        self.assertEqual(map_urls(site_root, all_urls), valid_urls)
