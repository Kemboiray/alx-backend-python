#!/usr/bin/env python3
"""Unit tests for utils module"""
import unittest
from unittest.main import main
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


if __name__ == "__main__":
    main()