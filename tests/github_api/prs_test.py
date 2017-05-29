import unittest

from github_api import prs, API


class TestPRMethods(unittest.TestCase):
    def test_statuses_returns_passed_travis_build(self):
        test_data = [[{"state": "success",
                     "context": "continuous-integration/travis-ci/pr"}],
                     [{"state": "success",
                       "context": "continuous-integration/travis-ci/pr"},
                      {"state": "failure",
                       "context": "chaosbot"}],
                     ]
        pr = "/repos/test/blah"

        for statuses in test_data:
            class Mocked(API):
                def __call__(m, method, path, **kwargs):
                    self.assertEqual(pr, path)
                    return statuses

            api = Mocked("user", "pat")
            url = "{}{}".format(api.BASE_URL, pr)

            self.assertTrue(prs.has_build_passed(api, url))

    def test_statuses_returns_failed_travis_build_in_wrong_context(self):
        test_data = [[{"state": "pending",
                       "context": "some_other_context"}],
                     [{"state": "success",
                       "context": "some_other_context"}],
                     [{"state": "error",
                       "context": "some_other_other_context"}],
                     ]
        pr = "/repos/test/blah"

        for statuses in test_data:
            class Mocked(API):
                def __call__(m, method, path, **kwargs):
                    self.assertEqual(pr, path)
                    return statuses

            api = Mocked("user", "pat")
            url = "{}{}".format(api.BASE_URL, pr)

            self.assertFalse(prs.has_build_passed(api, url))

    def test_statuses_returns_failed_travis_build_in_correct_context(self):
        test_data = [[{"state": "error",
                     "context": "continuous-integration/travis-ci/pr"}],
                     [{"state": "pending",
                       "context": "continuous-integration/travis-ci/pr"}],
                     ]
        pr = "/repos/test/blah"

        for statuses in test_data:
            class Mocked(API):
                def __call__(m, method, path, **kwargs):
                    self.assertEqual(pr, path)
                    return statuses

            api = Mocked("user", "pat")
            url = "{}{}".format(api.BASE_URL, pr)

            self.assertFalse(prs.has_build_passed(api, url))
