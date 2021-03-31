#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
import pep8


class TestDBStorage(unittest.TestCase):
    """ Class to test the console method """

    def test_Pep8(self):
        """
        test_pep8
        test for pep8
        """
        pep8val = pep8.StyleGuide(quiet=True)
        pep8checks = pep8val.check_files(["models/engine/db_storage.py"])
        self.assertEqual(pep8checks.total_errors, 0, "pep8 fail")
