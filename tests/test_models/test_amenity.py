#!/usr/bin/python3
"""test for amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """this will test the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.amenity

    def test_pep8_Amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
