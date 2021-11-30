#File to handle all the functions involved in user.py

import mysql.connector
import sys

#globalUser = 'p1'

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

cursor.execute("SELECT * FROM users")

result = cursor.fetchall()

for x in result:
    print(x)

cursor.close()
connection.close()

def initialMenu():
    print('1: Login')
    print('2: Create Account')
    print('3: Exit Program')

    menu = input("Enter Integer of Menu to enter: ")
    print()

    if menu == '1':
        print("Enter Username: ")
        username = input()
        password = input("Enter Password: \n")
        valid = login(username, password)
        print()

        if valid == 1:
            userMenu(username)
        else:
            print("Invalid Login.\n")
            initialMenu()

    elif menu == '2':
        print('Enter Username: ')
        username = input()
        if username == '':
            print('Invalid input. Returning to Main Menu.\n')
            initialMenu()
        password = input("Enter Password: ")
        if password == '':
            print('Invalid input. Returning to Main Menu.\n')
            initialMenu()
        createUser(username, password)
        #userMenu(username)
    elif menu == '3':
        sys.exit()
    else:
        print('invalid input')
        initialMenu()

def login(user, password):
    localUserName = user
    localPassword = password
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
    # cursor.execute("SELECT * FROM users")
    query = ("SELECT username, password FROM users WHERE username = %s")
    data = (localUserName, )
    cursor.execute(query, data)
    result = cursor.fetchall()

    for x in result:
        #if localUserName == x[1] and localPassword == x[3]:
        if localUserName == x[0] and localPassword == x[1]:

            return 1
        else:
            return 0
    cursor.close()
    connection.close()


def createUser(username, password):
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
    #cursor.execute("INSERT INTO users (Username, Password) VALUES")
    query = "INSERT INTO users (Username, Password) VALUES (%s, %s)"
    data = (username, password)

    cursor.execute(query, data)
    connection.commit()
    print("User: " + username + " created. Exiting Program")
    cursor.close()
    connection.close()
    #initialMenu()
    sys.exit()

def userMenu(username):
    localUserName = username
    print('-----User Menu-----')
    print('1: Items')
    print('2: Cart Information')
    print('3: Account Information')
    print('4: Logout')
    print('5: Exit Program')

    selection = input('Enter Integer of Menu to Enter: ')
    print()

    if selection == '1':
        print()
        #userMenu()
    elif selection == '2':
        print()
    elif selection == '3':
        accountInfo(localUserName)
    elif selection == '4':
        print('Logging out user: ' + localUserName + '\n\n')
        initialMenu()
    elif selection == '5':
        sys.exit()
    else:
        print('Invalid Input\n')
        userMenu()

def accountInfo(username):
    localUserName = username
    print('-----Account Info-----')
    print('1: Edit Account Info')
    print('2: View Order History')
    print('3: Logout')
    print('4: Delete Account')
    print('5: Go Back')
    print('----------------------')

    selection = input('Enter Integer of Menu to Enter: ')

    if selection == '1':
        print()
        editAccount(localUserName)
    elif selection == '3':
        print('Logging out user: ' + localUserName + '\n\n')
        initialMenu()
    elif selection == '4':
        deleteAnswer = input('Are you sure you want to Delete?' + localUserName + '(Y/N)\n')
        if deleteAnswer == 'y' or deleteAnswer == 'Y':
            deleteAccount(localUserName)
        else:
            accountInfo(localUserName)
    elif selection == '5':
        print('Returning to Previous Menu\n')
        userMenu(localUserName)
    else:
        print('Invalid Input.\n')
        accountInfo(localUserName)

def editAccount(username):
    localUserName = username
    print('Edit Account ' + localUserName + ':')
    print('1: Update First Name')
    print('2: Update Last Name')
    print('3: Update Credit Card Number')
    print('4: Update Shipping Address')
    print('5: Go Back')


    selection = input('Enter Integer of Information to Update: ')

    if selection == '1':
        update = input('Enter new FirstName: ')
        if update == '':
            print('Invalid input. Returning to Edit Account Menu\n')
            editAccount(localUserName)
        else:
            editFName(localUserName, update)
    elif selection == '2':
        update = input('Enter new LastName: ')
        if update == '':
            print('Invalid input. Returning to Edit Account Menu\n')
            editAccount(localUserName)
        else:
            editLName(localUserName, update)
    elif selection == '5':
        print('Returning to Previous Menu\n')
        accountInfo(localUserName)

def editFName(username, update):
    localUserName = username
    localUpdate = update
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
    query = "UPDATE users SET FirstName = %s WHERE Username = %s"
    data = (localUpdate, localUserName)

    print('User: ' + localUserName + ' changed FirstName to: ' + localUpdate + '\n')
    cursor.execute(query, data)
    connection.commit()
    sys.exit()


def editLName(username, update):
    localUserName = username
    localUpdate = update
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
    query = "UPDATE users SET LastName = %s WHERE Username = %s"
    data = (localUpdate, localUserName)

    print('User: ' + localUserName + ' changed LastName to: ' + localUpdate + '\n')
    cursor.execute(query, data)
    connection.commit()
    sys.exit()


def deleteAccount(username):
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
        ## exits the program if unsuccessful
        sys.exit()

    cursor = connection.cursor()

    query = "DELETE FROM users WHERE username = %s"
    data = (localUserName, )

    cursor.execute(query, data)
    connection.commit()

    print('Account: ' + localUserName + ' Deleted. Exiting Program')
    cursor.close()
    connection.close()
    #initialMenu()
    sys.exit()