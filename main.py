import mysql.connector


# main menu
print('Please enter one of the menu options below:')
print('1: Login')
print('2: Exit')

menu = input('enter a value: ')
#print(menu1)

if menu == '1':
    print("Login in please")
elif menu == '2':
    print('Exiting')
else:
    print('invalid input')