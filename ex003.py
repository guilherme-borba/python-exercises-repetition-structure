"""Write a program that reads and validates the following information:
1-Name: greater than 3 characters;
2-Age: between 0 and 150;
3-Salary: greater than zero;
4-Sex: 'f' or 'm';
5-Marital Status: 's', 'c', 'v', 'd';"""

while True:
    name = input('Enter the name: ')

    if len(name) <= 3:
        print('Error, name needs to be longer!')
    else:
        break

while True:
    age = int(input('Enter you age: '))

    if 0 <= age <= 150:
        break
    else:
        print('Error, age invalid!')

while True:
    salary = float(input('Enter your salary: '))

    if salary < 0:
        print('Error, salary invalid!')
    else:
        break

while True:
    sex = input('Enter your sex [F or M]: ').upper()

    if not(sex == 'F' or sex == 'M'):
        print('Error, sex invalid!')
    else:
        break

while True:
    marital_status = input('Enter a marital status [S, C, V or D]: ').upper()

    if not (marital_status == 'S' or marital_status == 'C' or marital_status == 'V' or marital_status == 'D'):
        print('Error, marital status invalid!')
    else:
        break
