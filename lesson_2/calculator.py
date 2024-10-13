# Ask the user for two numbers. => user will input 2 parameter values into function via the input
# Ask the user for the type of operation to perform: add, subtract, multiply or divide.
# Perform the calculation and display the result
#
# steps to programming:
# 1. use input to ask user for the first number
# 2. use input to ask user for the second number
# 3. use input to ask user for the operation type
# 4. Do the operation based on ops type on the first and second numbers
# 5. print the results

def perform_operations():
    print('Welcome to Calculator!')
    while True:
        first_number = input('Please enter a integer value: ')
        second_number = input('Please enter another integer value: ')
        operation_type = input(
            'Please enter a type of operation to perform from the following:'+
            'add, subtract, multiply or divide: ')
        if first_number.isnumeric() and second_number.isnumeric():
            result = 'The result is: '
            match operation_type:
                case 'add':
                    result += str(int(first_number) + int(second_number))
                case 'subtract':
                    result += str(int(first_number) - int(second_number))
                case 'multiply':
                    result += str(int(first_number) * int(second_number))
                case 'divide':
                    if int(second_number):
                        result += str(int(first_number) / int(second_number))
                    else:
                        result += 'Does not Exists!'
                case _:
                    print('Please enter the allowed operations type.')
            print(result)
        else:
            print('Please enter in only integer values.')
perform_operations()
