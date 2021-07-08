from models import (Base, session, Book, engine)
import datetime
import csv
import time


def menu():
    while True:
        print('''
            \nPROGRAMMING BOOKS
            \r1) Add book
            \r2) View all books
            \r3) Search for book
            \r4) Book Analysis
            \r5) Exit''')
        choice = input("What would you like to do?\n")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
            # hardcoded like this without try/except since only few options
            # return always stops a loop
        else:
            input('''
                    \rPlease choose one of the options above.
                    \rA number from 1-5.
                    \rPress enter to try again.''')
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
def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    # cuts the date on the space (October/25,/2017)
    try:
        month = int(months.index(split_date[0]) + 1)
        # goes into the list and checks what the index is (+1 due to zero-index)
        day = int(split_date[1].split(',')[0])
        # we only want the first part, hence the final [0]
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    except ValueError:
        input('''
            \n***** DATE ERROR *****
            \rThe date format shout include a valid Month Date, from the past
            \rEx: January 13, 2003
            \rPress enter to try again
            \r**********************''')
        return
    else:
        return return_date


def clean_price(price_str):
    try:
        price_float = float(price_str)
    except ValueError:
        input('''
            \n***** PRICE ERROR *****
            \rThe price should be a number without a currency symbol
            \rEx: 10.99
            \rPress enter to try again
            \r***********************''')
    else:
        return int(price_float * 100)
    # the * 100 is to get rid of the decimal


def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            # here we check if the book is already in the db
            # returns one if there is one or none if there is none
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, date_published=date, price=price)
                session.add(new_book)
        session.commit()


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            title = input('Title: ')
            author = input('Author: ')
            date_error = True
            while date_error:
                date = input('Published Date (Ex: October 25, 2017): ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error: False
            price_error = True
            while price_error:
                price = input('Price (Ex: 25.64): ')
                price = clean_price(price)
                if type(price) == int:
                    price_error = False
            new_book = Book(title=title, author=author, date_published=date, price=price)
            session.add(new_book)
            session.commit()
            print('Book added!')
            time.sleep(1.5)
        elif choice == '2':
            # view books
            for book in session.query(Book):
                print(f'{book.id}) | {book.title} | {book.author}')
            input('\nPress enter to return to the main menu.')
        elif choice == '3':
            # search
            pass
        elif choice == '4':
            # analysis
            pass
        else:
            print('GOODBYE')
            app_running = False
            # turns off the app



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    app()

    for book in session.query(Book):
        print(book)
