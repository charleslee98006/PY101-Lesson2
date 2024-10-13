'''
    Program to start taking inputs for car loan
'''
def car_loan_calculator():
    '''
        Car loan initialization for calculator
    '''
    while True:
        loan_amount = input('What is the loan amount? ')
        monthly_interest_rate = input('What is the monthly interest rate in percentages? ')
        loan_duration_in_months = input('What is the loan duration in months? ')
        if is_value_number(
            loan_amount,
            monthly_interest_rate,
            loan_duration_in_months) and is_values_greater_than_zero(
            loan_amount, monthly_interest_rate, loan_duration_in_months):
            total = fomula_calculation(
                float(loan_amount),
                float(monthly_interest_rate)/100,
                float(loan_duration_in_months))
            print(total)
            print(f'The result is: ${total:0.2f}\n')

def fomula_calculation(loan_amount, monthly_interest_rate,
                       loan_duration_in_months):
    '''
        Calculate the car loan based on the input 
    '''
    return loan_amount * ((monthly_interest_rate/12) / (
        1 - (1 + (monthly_interest_rate/12)) **
        (-loan_duration_in_months)))

def is_value_number(value1, value2, value3):
    '''
        Checks to see if value is a float or integer
    '''
    try:
        number1 = float(value1)
        number2 = float(value2)
        number3 = float(value3)
        if number1 == 'nan' or number2 == 'nan' or number3 == 'nan':
            print('Values are not a number. Please use numbers instead of words.')
            return False
        return True
    except ValueError:
        print('Please use integers or decimal value numbers only')
        return False

def is_values_greater_than_zero(value1, value2, value3):
    '''
        Checks to see if value is greater than zero
    '''
    if (float(value1) > 0) and (float(value2) > 0) and (float(value3) > 0):
        return True
    return False

car_loan_calculator()
