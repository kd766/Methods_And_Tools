import mysql.connector
import user
import item
import cart


# main menu
user.initialMenu()

#user.initialMenu()


#print('Please enter one of the menu options below:')
# print('1: Login')
# print('2: Create Account')
# print('3: Exit Program')

# menu = input("Enter Integer of Menu to enter: ")

# if menu == '1':
#     print("Enter Username: ")
#     username = input()
#     password = input("Enter Password: \n")
#     valid = user.login(username, password)
#     print()

#     if valid == 1:
#         #print("new menu")
#         user.userMenu()
#     else:
#         print("Invalid Login. Exiting Program")
#         exit()

# elif menu == '2':
#     print('Enter Username: ')
#     username = input()
#     password = input("Enter Password: ")
#     user.createUser(username, password)
#     user.userMenu()
# else:
#     print('invalid input')
