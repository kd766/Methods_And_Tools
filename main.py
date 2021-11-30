import mysql.connector
import user


# main menu
print('Please enter one of the menu options below:')
print('1: Login')
print('2: Create Account')
print('3: Exit')

menu = input()
#print(menu1)

if menu == '1':
    print("Enter Username: ")
    username = input()
    password = input("Enter Password: \n")
    valid = user.login(username, password)
    print()
    #print(valid)

    if valid == 1:
        print("new menu")
    else:
        print("Invalid Login")
        exit()

elif menu == '2':
    print('Enter Username: ')
    username = input()
    password = input("Enter Password: ")
    user.createUser(username, password)
else:
    print('invalid input')

#user.say_hello()