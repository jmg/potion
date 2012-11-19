from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Unicode, Integer
from sqlalchemy import create_engine

from utils import is_subclass, is_instance, load_module

BaseEntity = declarative_base()
metadata = BaseEntity.metadata


class Entity(object):

    pass


class Field(object):

    def __init__(self, field_type):

        self.field_type = field_type


def get_entities(name, path=None):

    models = load_module(name, path=path)
    return [model for name, model in models.__dict__.iteritems() if is_subclass(model, Entity)]


def setup_entities(entities):

    sql_slchemy_entities = []

    for entity in entities:

        attrs = {}        

        for name, field in entity.__dict__.iteritems():
            if is_instance(field, Field):
                attrs[name] = Column(name, field.field_type)

        attrs.setdefault("id", Column(Integer, primary_key=True))
        attrs.setdefault("__tablename__", entity.__name__)

        sql_slchemy_entities.append(type("Model", (BaseEntity, ), attrs))

    return sql_slchemy_entities


def create_all():

    metadata.create_all()