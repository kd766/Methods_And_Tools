#file for user.py

#Create table
conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY, 
		password String,
		userName String,
		firstName String,
		lastName String,
		address1 Strjng,
    admin bool, 
		payment integer
		)''')
