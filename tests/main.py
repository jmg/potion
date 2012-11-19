import unittest
from os import remove
import os.path

from potion import potion

class TestBase(unittest.TestCase):

    def setUp(self):

        potion.entities = []
        potion.sqlalchemy_entities = []

    def test_get_entities(self):

        entities = potion.get_entities("models", path="tests")
        self.assertTrue(len(entities))

        for entity in entities:
            self.assertTrue(issubclass(entity, potion.Entity))
        
    def test_create_entities(self):

        entities = potion.get_entities("models", path="tests")

        db_name = "test.sqlite"

        if os.path.isfile(db_name):
            remove(db_name)

        sql_alchemy_entities = potion.setup_entities(entities)

        self.assertTrue(len(sql_alchemy_entities))
        for entity in sql_alchemy_entities:
            self.assertTrue(issubclass(entity, potion.BaseEntity))

        potion.metadata.bind = potion.create_engine('sqlite:///{db}'.format(db=db_name))
        potion.create_all()

        self.assertTrue(os.path.isfile(db_name))

    def test_create_entities_user_api(self):

        if os.path.isfile("db.sqlite"):
            remove("db.sqlite")

        #User example
        from models import Book

        potion.metadata.bind = potion.create_engine('sqlite:///db.sqlite')
        potion.create_all()
        #End user example

        self.assertTrue(os.path.isfile("db.sqlite"))