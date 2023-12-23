#!/usr/bin/python3
"""contains Test for base_model class"""
import os
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
from unittest.mock import patch
import models


class test_basemodel(unittest.TestCase):
    """Test cases for base_model class """

    def __init__(self, *args, **kwargs):
        """Class constructor for base_model """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Set up for base_model class """
        self.instance = BaseModel()

    def tearDown(self):
        """Tear down for base_model"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Tests whether the type of the istance
        'i' is equal to the expected type"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test for Keyworded arguments """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Checks for type error """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Testing str representation of object """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Testing dictionary representation of object """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Testing Kwargs with None """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip("Test Not necessary")
    def test_kwargs_one(self):
        """Test kwargs with one argument """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Testing id to be sure its a string """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Testing created_at """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Testing Updated_at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_delete_method(self):
        """ Test delete method """
        with patch.object(models.storage, 'delete') as mock_delete:
            self.instance.delete()
            mock_delete.assert_called_once_with(self.instance)
