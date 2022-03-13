import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username, password)")

def get_users():
	queryset = cursor.execute("SELECT * FROM users")
	users = queryset.fetchall()
	return users

def login():
	username = input("Podaj swój login: ")
	password = input("Podaj swoje hasło: ")
	queryset = cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?" , (username, password))
	result = queryset.fetchone()
	connection.commit()
	print('wynik = ', result)
	return result

def delete():
	username = input("Podaj login:")
	queryset = cursor.execute("DELETE FROM users WHERE username = ?", [username])
	result = queryset.fetchone()
	connection.commit()
	print("usunięte")

def update():
	username = input("Podaj login:")
	password = input("Podaj nowe hasło: ")
	queryset = cursor.execute("UPDATE users SET password = ? WHERE username = ? ", (password, username))
	result = queryset.fetchone()
	connection.commit()
	print("zmieniono")

while True:
	print('1. Zarejestruj się')
	print('2. Zobacz uzytkownikow')
	print('3. Zaloguj się')
	print('4. Usuń uzytkownika')
	print('5. Zmodyfikuj uzytkownika')
	print('0. Wyjdź z programu')
	option = input('Wybierz opcję: ')
	if option == "1":
		username = input("Podaj swój login: ")
		password = input("Podaj swoje hasło: ")
		cursor.execute("INSERT INTO users VALUES ( ? , ? )" , (username , password))
		connection.commit()
	elif option == "2":
		print(get_users())
	elif option == "3":
		login()
	elif option == "4":
		delete()
	elif option == "5":
		update()
	elif option == "0":
		connection.close()
		break