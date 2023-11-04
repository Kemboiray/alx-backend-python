#!/usr/bin/env python3
"""This module defines tests for module `client`"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """This class defines tests for `GithubOrgClient`'s methods"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json", return_value={"repos_url": "google.com"})
    def test_org(self, org: str, mock_get_json):
        sample = GithubOrgClient(org)
        self.assertEqual(sample.org, mock_get_json.return_value)
        sample.org
        mock_get_json.assert_called_once()
    # sample = GithubOrgClient(org)
