#!/usr/bin/python3
"""Test for City Class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Test cases for city class """

    def __init__(self, *args, **kwargs):
        """constructor method of the class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Testing city id """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Testing City Name """
        new = self.value()
        self.assertEqual(type(new.name), str)
