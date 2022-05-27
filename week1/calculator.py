# Write a simple Python calculator
# By Peter Edoka Augustine - I4G0133560UA

# Write a Python calculator that can perform: addition, subtraction, division,
# multiplication and modulus operations. It should accept user input

def calculate():
    print('Please select an option:')
    action = input('''1 >> Addition;
2 >> Subtraction;
3 >> Division;
4 >> Multiplication;
5 >> Modulus;
To exit, press 0.

''')
    if action in ['1', '2', '3','4', '5']:
        print('Enter the two numbers')  
        num1 = float(input('Enter the first number: \n'))
        num2 = float(input('Enter the second number: \n'))
        if action == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif action == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif action == '3':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif action == '4':
            print(f"{num1} X {num2} = {multiply(num1, num2)}")
        elif action == '5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
    elif action == '0':
        print('Good bye')
    else:
        print('!!!!!!!!!!!!!!!!!!!!!')
        print('invalid input')
        print('!!!!!!!!!!!!!!!!!!!!!')
        calculate()
    again_check = input('Do you want to perform another action> (yes/no)\n')

    if again_check == 'yes':
        calculate()
    else:
        print('Good bye')

def add(a, b):
    return (a + b)

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def modulus(a, b):
    return a % b

calculate()