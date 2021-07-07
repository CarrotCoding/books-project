from models import (Base, session, Book, engine)

# import models
# main menu
    # add, search, analysis, exit, view
# functions
    # add books to the database
    # delete books
    # search books
    # data cleaning
# loop runs program
    # when user exits it stops


if __name__ == '__main__':
    Base.metadata.create_all(engine)
