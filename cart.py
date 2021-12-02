#file to handle the access to the cart

import mysql.connector
import sys
import user
import item

def cartMenu(username):
    localUserName = username

    print('-----Cart Information-----')
    print('User: ' + localUserName)
    print('1: View Cart')
    print('2: Add or Remove Items')
    print('3: Checkout')
    print('4: Go Back')
    print('--------------------------')

    selection = input('Enter Integer of Menu to Enter: \n')

    if selection == '1':
        print()
        viewCart(localUserName)
    elif selection == '2':
        item.initialItemMenu(localUserName)
    elif selection == '3':
        print('Checkout')
        checkout(localUserName)
    elif selection == '4':
        print('Returning to Previous Menu\n')
        user.userMenu(localUserName)
    else:
        print('\nInvalid input.')
        cartMenu(localUserName) 

def viewCart(username):
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
    query = ('SELECT books.ISBN, books.Title FROM users, books, cart WHERE cart.cartUser = %s AND users.Username = cart.cartUser AND books.ISBN = cart.cartISBN')
    data = (localUserName, )

    cursor.execute(query, data)
    result = cursor.fetchall()

    print('Viewing cart for user: ' + localUserName)
    print('-----------------------------------')
    for x in result:
        print(x)
    cursor.close()
    connection.close()
    print()
    item.initialItemMenu(localUserName)

def addItemToCart(username):
    localUserName = username

    book = input('Enter ISBN of Book you want to Add: \n')

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
    query = ('INSERT INTO cart (cartUser, cartISBN) VALUES (%s, %s)')
    data = (localUserName, book)

    cursor.execute(query, data)
    connection.commit()
    print('Book with ISBN: ' + book + ' added to cart for user: ' + localUserName + '\n')
    cursor.close()
    connection.close()

    item.initialItemMenu(localUserName)

def removeItemFromCart(username):
    localUserName = username

    book = input('Enter ISBN of book to remove: \n')

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
    query = ('DELETE FROM cart WHERE cartUser = %s AND cartISBN = %s')
    data = (localUserName, book)

    cursor.execute(query, data)
    connection.commit()

    print('Book with ISBN: ' + book + ' removed from cart for user: ' + localUserName + '\n')
    cursor.close()
    connection.close()
    
    item.initialItemMenu(localUserName)

def checkout(username):
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

    # Insert the items from the cart into the order history
    query = "INSERT INTO pastorders (orderUser, orderISBN) SELECT cartUser, cartISBN FROM cart WHERE cartUser = %s"
    data = (localUserName, )

    cursor.execute(query, data)
    connection.commit()
    print('Adding order to order history')
    cursor.close()

    # update the quantity of the items
    cursor = connection.cursor()

    query = "UPDATE books SET Quantity = Quantity - 1 WHERE ISBN = ANY (SELECT cartISBN FROM cart WHERE cartUser = %s)"
    data = (localUserName, )

    cursor.execute(query, data)
    connection.commit()
    cursor.close()

    # Delete the items that are in the cart
    cursor = connection.cursor()
    query = "DELETE FROM cart WHERE cartUser = %s"
    data = (localUserName, )

    cursor.execute(query, data)
    connection.commit()
    print("Deleting the items from cart")

    cursor.close()
    connection.close()
    #sys.exit()
    item.initialItemMenu(localUserName)

def pastItems(username):
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
    query = ('SELECT books.ISBN, books.Title FROM users, books, pastorders WHERE pastorders.orderUser = %s AND users.Username = pastorders.orderUser AND books.ISBN = pastorders.orderISBN')
    data = (localUserName, )

    cursor.execute(query, data)
    result = cursor.fetchall()

    print('Viewing Past Items Purchased for user: ' + localUserName)
    print('-----------------------------------')
    for x in result:
        print(x)
    print()
    cursor.close()
    connection.close()
    user.accountInfo(localUserName)
