import unittest
from os import remove
import os.path

from potion import potion

class TestBase(unittest.TestCase):

    def setUp(self):

        self.entities = potion.get_entities("models", path="tests")

    def test_get_entities(self):

        self.assertTrue(len(self.entities))

        for entity in self.entities:
            self.assertTrue(issubclass(entity, potion.Entity))
        
    def test_create_entities(self):

        db_name = "test.sqlite"

        if os.path.isfile(db_name):
            remove(db_name)

        sql_alchemy_entities = potion.setup_entities(self.entities)

        self.assertTrue(len(sql_alchemy_entities))
        for entity in sql_alchemy_entities:
            self.assertTrue(issubclass(entity, potion.BaseEntity))

        potion.metadata.bind = potion.create_engine('sqlite:///{db}'.format(db=db_name) )
        potion.create_all()

        self.assertTrue(os.path.isfile(db_name))