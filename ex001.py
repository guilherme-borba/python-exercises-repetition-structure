"""Write a program that asks for a note, between zero and ten. Show a message if the value is invalid and
continue asking until the user enters a valid value."""

while True:
    note = int(input('Enter a number, between zero and ten: '))
    if 0 <= note <= 10:
        break
