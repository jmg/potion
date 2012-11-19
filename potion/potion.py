from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Unicode, Integer
from sqlalchemy import create_engine

from utils import is_subclass, is_instance, load_module

BaseEntity = declarative_base()
metadata = BaseEntity.metadata

entities = []
sqlalchemy_entities = []


class EntityMeta(type):

    def __init__(cls, name, bases, dct):

        if not cls in entities:
            entities.append(cls)


class Entity(object):

    __metaclass__ = EntityMeta


class Field(object):

    def __init__(self, field_type):

        self.field_type = field_type


def get_entities(name, path=None):

    models = load_module(name, path=path)
    return [model for name, model in models.__dict__.iteritems() if is_subclass(model, Entity)]


def setup_entities(potion_entities):

    for entity in potion_entities:

        attrs = {}        

        for name, field in entity.__dict__.iteritems():
            if is_instance(field, Field):
                attrs[name] = Column(name, field.field_type)

        attrs.setdefault("id", Column(Integer, primary_key=True))
        attrs.setdefault("__tablename__", entity.__name__)

        sqlalchemy_entities.append(type("Model", (BaseEntity, ), attrs))

    return sqlalchemy_entities


def clean_entities():

    return [entity for entity in entities if not entity is Entity]


def create_all():
    
    if not sqlalchemy_entities:

        potion_entities = clean_entities()
        setup_entities(potion_entities)

    metadata.create_all()