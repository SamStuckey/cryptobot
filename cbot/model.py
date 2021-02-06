from cbot.db                    import CRUD
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Model(Base, CRUD):
    pass
