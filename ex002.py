"""Write a program that reads a username and password and does not accept
the password that is the same as the username, showing an error message and asking for the information again."""

name = input('Enter the name: ').lower()
while True:
    password = input('Enter the password: ').lower()

    if password == name:
        print('Error, type again!')
    else:
        break
