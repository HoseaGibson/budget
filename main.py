# Import
import budget_calc
# Declare Variables
# Get user input for monthly cash
from output_excel import create_workbook

monthly = int(input("How much is your monthly cash flow " ))

# Do calculation for 50%
essential = budget_calc.budget_50(monthly)

print(essential)
# Do calculation for 30%
wants = budget_calc.budget_30(essential)

print(wants)
# Do calculation for 20%

savings = budget_calc.budget_20(wants)

print(savings)
# Ask user if they have a goal and how much they want to put from 20% savings
goals = input("Do you have a goal you are trying to save for? 'yes' or 'no' ")
if goals == 'yes':
    amount = float(input("what is your goal amount to save? "))
    goal_amount = wants - amount
    print(goal_amount)
else:
    print("you have no goals for this month")
# Ask user how much do they plan total to save and print how long it will take to get there
# or if they know the month calc how much they need to save to reach that goal
# Save to a pdf file for all information
create_workbook()
