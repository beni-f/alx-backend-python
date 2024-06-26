#!/usr/bin/env python3
"""
    Parameterize a unit test
"""
import unittest
from unittest.mock import patch, Mock
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
        Tests the access_nested_map method from utils.py file
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ Test """
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the utils.get_json method"""
    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """ Test """
        test_cases = [
            ('http://example.com', {"payload": True}),
            ('http://holberton.io', {"payload": False})
        ]

        for test_url, test_payload in test_cases:
            response = Mock()
            response.json.return_value = test_payload
            mock_get.return_value = response

            result = utils.get_json(test_url)

            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()
        ins = TestClass()
        with patch.object(ins, 'a_method', wraps=ins.a_method) as mock:
            result1 = ins.a_property
            result2 = ins.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock.assert_called_once()
