#!/usr/bin/env python3
"""Unit tests for utils module"""
import unittest
# import utils
from unittest.main import main
from unittest.mock import patch, MagicMock
from utils import *
from parameterized import parameterized
from typing import Tuple, Dict, Any


class TestAccessNestedMap(unittest.TestCase):
    """Define a test for ``access_nested_map``"""

    @parameterized.expand([({
        "a": 1
    }, ("a", ), 1), ({
        "a": {
            "b": 2
        }
    }, ("a", ), {
        "b": 2
    }), ({
        "a": {
            "b": 2
        }
    }, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple,
                               expected: Any):
        """Test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a", )), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple):
        """Test that a KeyError is raised"""
        with self.assertRaises(KeyError) as ke:
            access_nested_map(nested_map, path)
            self.assertIn(ke.exception.args[0], path)


class TeseGetJson(unittest.TestCase):
    """This class encapsulates a test for the ``get_json`` function"""

    @parameterized.expand([("http://example.com", {
        "payload": True
    }), ("http://holberton.io", {
        "payload": False
    })])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """Test ``get_json``"""
        with patch("utils.requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            self.assertEqual(get_json(test_url), test_payload)


if __name__ == "__main__":
    main()
