#File to handle all the functions involved in item.py

import mysql.connector
import sys
import user
import cart

def initialItemMenu(username):
    localUserName = username
    print('-----Item Menu-----')
    print('1: View All Books')
    print('2: View Cart')
    print('3: Add Item to Cart')
    print('4: Remove Item from Cart')
    print('5: Go Back')

    selection = input('Enter Integer of Menu to Enter: \n')

    if selection == '1':
        viewAllBooks(localUserName)
    elif selection == '2':
        print()
        cart.viewCart(localUserName)
    elif selection == '3':
        print()
        cart.addItemToCart(localUserName)
    elif selection == '4':
        print()
        cart.removeItemFromCart(localUserName)
    elif selection == '5':
        print('\nReturning to Previous Menu\n')
        user.userMenu(localUserName)
    else:
        print('\nInvalid input.\n')
        initialItemMenu(localUserName)


def viewAllBooks(username):
    localUserName = username

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="methods"
        )
    except:
        print("Failed connection.")
        sys.exit()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")

    result = cursor.fetchall()

    print('\nBooks: ISBN, Title, Author, Genre, Quantity')
    print('----------------------------------------')
    for x in result:
        print(x)
    print()
    cursor.close()
    connection.close()

    initialItemMenu(localUserName)

def viewByTitle(username):
    localUserName = username

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="methods"
        )
    except:
        print("Failed connection.")
        sys.exit()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")

    result = cursor.fetchall()

    print()

def viewByAuthor(username):
    localUserName = username
    
    authorFname = input('Enter Author first name: \n')
    authorLname = input('Enter Author last name: \n')

    if authorFname == '' or authorLname == '':
        print('Invalid Input\n')
        viewByAuthor(localUserName)
    else:
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="methods"
            )
        except:
            print("Failed connection.")
            sys.exit()

        cursor = connection.cursor()
        query = ("SELECT * FROM books WHERE Author = '%s %s'")
        data = (authorFname, authorLname)
        cursor.execute(query, data)
        #cursor.execute("SELECT * FROM books WHERE Author = '%s %s'")


        result = cursor.fetchall()

        print('\nBooks from author ' + author + ':')
        print('---------------------------------')
        for x in result:
            print(x)
        print()
        cursor.close()
        connection.close()

        initialItemMenu(localUserName)
