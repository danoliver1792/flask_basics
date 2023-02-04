from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# creating SQL Lite
engine = create_engine("sqlite:///atividades.db")
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


# creating the table
class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(45), index=True)
    age = Column(Integer)

    def __repr__(self):
        return "<People {}>".format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Activity(Base):
    __tablename__ = "activity"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    people_id = Column(Integer, ForeignKey("people.id"))
    people = relationship("People")


# creating the database
def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
