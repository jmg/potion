from potion.potion import Entity, Field, Unicode

class Book(Entity):

    title = Field(Unicode(255))
    author = Field(Unicode(255))
