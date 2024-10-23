from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import  sessionmaker, declarative_base


db_string = 'sqlite:///maindb.db'
engine = create_engine(db_string)
engine.connect()


S = sessionmaker(bind=engine)
session = S()


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f'(id = {self.id}) User: {self.username}'


Base.metadata.create_all(bind=engine)