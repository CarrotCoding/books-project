from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///books.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    # the 'Title' is how it's shown in the database
    author = Column('Author', String)
    date_published = Column('Published', Date)
    price = Column('Price', Integer)

    def __repr__(self):
        return f'Title: {self.title}, Author: {self.author}, Published: {self.date_published}, Price: {self.price}'
