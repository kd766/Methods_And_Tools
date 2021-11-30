#file for user.py
#class User:
import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="methods"
    )
    print("Successful connection.")
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

def say_hello():
    print("Hello")



def login(user, password):
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

    if user == x[1] and password == x[4]:
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

