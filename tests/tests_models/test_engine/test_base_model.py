#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str(self):
        instance = BaseModel()
        expected_string = "[BaseModel] ({}) {}".format(
            instance.id, instance.__dict__)
        self.assertEqual(str(instance), expected_string)

    def test_save(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertIsInstance(datetime.strptime(
            instance_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertIsInstance(datetime.strptime(
            instance_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)


if __name__ == '__main__':
    unittest.main()
