import math

#investment and bond definitions
MENU = " investment - to calculate the amount of interest you'll earn on your investment. \
         bond - to calculate the amount you'll have to pay on a home loan. "
#output the menu
print(MENU)

#user chooses which calculation to run
choice = input(" Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#user chooses investment
if choice == 'investment':
#user inputs the deposit amount
    p = float(input("Enter the amount of money you want to deposit: "))
#user inputs the annual interest rate    
    interest_rate = float(input("Please enter your annual percentage of interest rate: "))
#user inputs the period of investment    
    t = float(input("Please enter the number of years you plan on investing: "))
#calculate the percentage of annual interest rate    
    r = interest_rate / 100
#user chooses the type of interest
    interest = input("Do you want a simple interest or a compound interest? ").lower()
#user adopts the simple interest choice
    if interest == "simple" :
    #calculate the simple interest
        A = p * (1 + r * t)
    #print out the outcome
        print(f"with simple interest after {t} years you will be given a total amount of: {A:.2f}")
#user adopts the compound interest choice    
    elif interest == "compound" :
    #calculate the compound interest
        A = p * math.pow((1+r),t)
#print out the outcome
        print(f"with compound interest after {t} years you will be given a total amount of: {A:.2f}")
    else:
        print("Please enter the right interest type: 'simple' or 'compound'.")

#user chooses bond
elif choice == 'bond':
#user inputs the present value of the house
    p = float(input("Please enter the present value of the house: "))
#user inputs thethe annual interest rate
    interest_rate_2 = float(input("Please enter your annual percentage of interest rate: "))
#calculate the annual interest rate
    i = (interest_rate_2 /100) /12
#user inputs the number of months to repay
    n = float(input("Please enter the number of months you plan to take to repay the bond: "))
#calculate the repayment
    repayment = (i * p) / (1 - (1 + i)**(-n))
#print out the outcome
    print(f"you will have to repay the amount of {repayment:.2f} per month.")
# wrong input
else:
    print("Invalid input, please enter 'investment' or 'bond'.")
