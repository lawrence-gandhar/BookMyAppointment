from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ======================================================================
#
# ======================================================================

ENGINE = create_engine('sqlite:///online_dental.sqlite', echo = True).connect()
DB_SESSION = sessionmaker(bind=ENGINE)

Base = declarative_base()
session = DB_SESSION()

# ======================================================================
#
# ======================================================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    username = Column(String(50), nullable=True, index=True)
    first_name = Column(String, nullable=True, index=True)
    last_name = Column(String, nullable=True, index=True)
    email = Column(String, nullable=True, index=True)
    logged_on = Column(String, nullable=True, index=True)
    is_online = Column(String, nullable=True, index=True)
    pin = Column(String, nullable=True, index=True)


    def __repr__(self):
        name = []

        if self.first_name is not None:
            name.append(self.first_name)
        if self.last_name is not None:
            name.append(self.last_name)

        return ''.join(name)

# ======================================================================
#
# ======================================================================
def create_db():
    print("create db")
    Base.metadata.create_all(ENGINE)

# ======================================================================
# INSERT DATA
# ======================================================================
def insert_data(obj = None):
    if obj is not None:
        session.add(obj)
        session.commit()
        return True
    return False


# ======================================================================
# SELECT DATA
# ======================================================================
def select_data(obj=None):
    if obj is not None:
        result = session.query(obj)

        for row in result:
            print(row)
    else:
        result = ()
