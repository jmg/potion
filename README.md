## Elixir-like declarative layer for sql-alchemy

------------------------------------------------------------------

Potion is a Elixir-like declarative layer for sql-alchemy.
 
So far it just cover a little bit of the functionality of the [elixir library](http://elixir.ematia.de/trac/wiki).

As Elixir was **not** maintaned for a long time and it does **not** support the latest versions of [sqlalchemy](http://www.sqlalchemy.org) this project aims to eventually replace it.

### Define a model

```python
""" models.py """

from potion import Entity, Field, Unicode

class Book(Entity):

    title = Field(Unicode(255))
    author = Field(Unicode(255))    
```

### Setup the database

```python
import potion
from models import *

potion.metadata.bind = potion.create_engine('sqlite:///db.sqlite')
potion.create_all()
```
