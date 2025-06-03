print("Welcome to the Compound interest calculator")

#initial_principal_balance = float(input("Enter your initial principal balance"))
#interest_rate = float(input("Enter the intrest rate"))
#number_of_time_periods_elapsed = int(input("Enter the number of time periods elapsed "))
#fianl_amount = initial_principal_balance*(1 + interest_rate / 100)**number_of_time_periods_elapsed

initial_principal_balance = 0
interest_rate = 0
number_of_time_periods_elapsed = 0

while initial_principal_balance <= 0:
    initial_principal_balance = float(input("Enter your initial principal balance "))
    if initial_principal_balance <= 0:
        print("Initial principal balance can not be equal to zero or less ")

while interest_rate <= 0:
    interest_rate = float(input("Enter the interest rate "))
    if interest_rate <= 0:
        print("interest rate can not be equal to zero or less ")

while number_of_time_periods_elapsed <= 0:
    number_of_time_periods_elapsed = int(input("Enter your number of time periods elapsed in years "))
    if number_of_time_periods_elapsed <= 0:
        print("number of time periods elapsed can not be equal to zero or less ")

final_amount = initial_principal_balance * (1 + interest_rate / 100)**number_of_time_periods_elapsed
print(f'Your initial principal balance : {initial_principal_balance}, final amount after {number_of_time_periods_elapsed} year/s is {final_amount}')


#Extra Check just for fun

#if initial_principal_balance > 0 and interest_rate > 0 and number_of_time_periods_elapsed > 0: 
#    final_amount = initial_principal_balance * (1 + interest_rate/100) ** number_of_time_periods_elapsed 
#    if final_amount < initial_principal_balance:
#        print(f'You lost money. Initial principal balance: {initial_principal_balance}, Final amount {final_amount:.2f}')
#    elif final_amount == initial_principal_balance:
#        print(f'Your money reamined the same. Initial principal balance: {initial_principal_balance}, Final amount {final_amount:.2f}')
#    elif final_amount > initial_principal_balance:
#        print(f'You gained money. Initial principal balance: {initial_principal_balance}, Final amount {final_amount:.2f}')
#else:
#    print("Error")