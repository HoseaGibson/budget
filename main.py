# Import
import budget_calc
# Declare Variables
# Get user input for monthly cash
monthly = int(input("How much is your monthly cash flow" ))

# Do calculation for 50%
total = budget_calc.budget_50(monthly)

print(total)
# Do calculation for 30%
total2 = budget_calc.budget_30(total)

print(total2)
# Do calculation for 20%

total3 = budget_calc.budget_20(total2)

print(total3)
# Ask user if they have a goal and how much they want to put from 20% savings
# Print to console
# Save to a pdf file for all information


