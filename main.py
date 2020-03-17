# Import
import budget_calc
from output_excel import create_workbook







# Get total monthly cash from check
while True:
    try:
        monthly = int(input("How much is your monthly cash flow " ))
        if monthly == 0:
            print("Please enter a non-zero number")
        elif monthly < 0:
            print("Please enter a positive number")
        break
    except ValueError:
        print("Please enter a valid number")
# Essential budget

essential = budget_calc.budget_50(monthly) # Calculates essential percentage
print(essential, str(" for the month"))

#Input varaibles essentials
mortgage_rent = int(input("How much is your housing for month: "))
util = int(input("How much is your utilities this month 'gas, power, etc': "))
food = int(input("How much is your groceries for month "))
health_insurance = int(input("How much is your health insurance for the month "))
car_payment = int(input("How much is your car payment"))

# Calculates total bills returns left over
e_total = budget_calc.budget_50_total(essential, mortgage_rent, util, food, health_insurance, car_payment)

# Savings budget
saving = budget_calc.budget_20(monthly)  # Calculates saving percentage

# Input variables saving
emergency_fund = int(input("How much is your saving for month': "))
ira_saving_401k = int(input("How much is your ira "))

# Calculates total bills returns left over
s_total = budget_calc.budget_20_total(saving, emergency_fund, ira_saving_401k) # Calculates total savings returns left over

# Wants budget
want = (budget_calc.budget_30(monthly)) # Calculates wants percentage

# Input variables wants
clothing = int(input("How much is your saving for shopping': "))
hobby = int(input("How much is your hobbies "))
dates = int(input("How much is your dining "))

# Calculates total bills returns left over
want_total = budget_calc.budget_30_total(want, clothing, hobby, dates)# Calculates total wants and returns left overs

# Set up for goals
goals = input("Do you have a goal to save for 'yes or no'")

g_total = budget_calc.isGoal(goals)

# Save to a pdf file for all information

create_workbook(mortgage_rent, util, food, health_insurance, car_payment, e_total, emergency_fund, ira_saving_401k, s_total,  clothing, hobby, dates, want_total, g_total )

